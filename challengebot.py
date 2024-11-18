import pygame
import os
import numpy as np
import sys

# import RPi.GPIO as GPIO
# import time

frame = 0
debug = False

def cart2pol(x, y):
    rho = np.sqrt(x**2 + y**2)
    phi = np.arctan2(y, x)
    return(rho, phi)

def pol2cart(rho, phi):
    x = rho * np.cos(phi)
    y = rho * np.sin(phi)
    return(x, y)

class Robot:
    def __init__(self, use_simulator=True):
        self.driver = SimulatorDriver()
        # if use_simulator:
        #     self.driver = SimulatorDriver()

        # else:
        #     self.driver = RealRobotDriver()  # driver can be a simulator or real robot

    def motors(self, left, right, seconds):
        self.driver.motors(left, right, seconds)
    
    def sonars(self):
        return self.driver.sonars()
    
    def exit(self):
        self.driver.exit()

# Simulator Driver
class SimulatorDriver:
    def __init__(self):
        self.origin = (300, 200)
        self.x = self.origin[0]  # Starting x position
        self.y = self.origin[1]  # Starting y position
        self.heading = 0 # pointing to the right
        self.left_motor_velocity = 0
        self.right_motor_velocity = 0
        self.radius = 20  # Robot radius for visualization
        self.robot_width = 200
        self.robot_height = 200
        size = 200
        self.img_left = pygame.image.load(os.path.join('img', "left", f"{size}", 'robobunny.png'))
        self.img_right = pygame.image.load(os.path.join('img', "right", f"{size}", 'robobunny.png'))
        self.img = self.img_left
        self.running = True
        self.clock = pygame.time.Clock()
        self.fps = 60
        self.box_width = 660 #mm
        self.box_height = 410 #mm
        self.max_x_box = self.box_width / 2 + self.origin[0]
        self.min_x_box = self.origin[0] - self.box_width / 2
        self.max_y_box = self.box_height / 2 + self.origin[1]
        self.min_y_box = self.origin[1] - self.box_height / 2

        self.start_simulation()

    def find_corners(self, x, y, heading):
        i = np.array([1, 2, 3, 4])
        angle_to_corner = np.arctan(self.robot_width / self.robot_height)
        phi = heading - angle_to_corner
        omega = np.sqrt((self.robot_height / 2)**2 + (self.robot_width / 2)**2)
        corner_offsets = pol2cart(omega, phi + np.radians(90) * i)
        corner_x_values = x + corner_offsets[0]
        corner_y_values = y + corner_offsets[1]
        return corner_x_values, corner_y_values

    def calculate_next_move(self, left, right, seconds):
        # for a certain number of seconds:
        degrees_per_frame = 0.98
        new_x = self.x
        new_y = self.y
        new_heading = self.heading
        # update position
        if right == 1 and left == -1:
            new_heading = (self.heading - degrees_per_frame) % 360
        elif right == -1 and left == 1:
            new_heading = (self.heading + degrees_per_frame) % 360
        elif right == left:
            if right == 0:
                pass
            else:
                speed = right * 1
                new_x += speed * np.cos(np.radians(self.heading))
                new_y -= speed * np.sin(np.radians(self.heading))

        return new_heading, new_x, new_y

    def motors(self, left, right, seconds):
        # power (+ / -) to left and right motors
        # number of seconds to maintain that

        # don't let the robot go through the box

        for _ in range(int(seconds * self.fps)):
            new_heading, new_x, new_y = self.calculate_next_move(left, right, seconds)
            corner_x_values, corner_y_values = self.find_corners(new_x, new_y, new_heading)
            biggest_x = np.max(corner_x_values)
            biggest_y = np.max(corner_y_values)
            smallest_x = np.min(corner_x_values)
            smallest_y = np.min(corner_y_values)
            x_crash = (biggest_x > self.max_x_box) or (smallest_x < self.min_x_box)
            y_crash = (biggest_y > self.max_y_box) or (smallest_y < self.min_y_box)
            if x_crash or y_crash:
                #throw error
                print("error")
            else:
                self.x = new_x
                self.y = new_y
                self.heading = new_heading

            self.render()
    
    def sonars(self):
        return 10

    def render(self):
        # Clear the screen
        self.screen.fill((255, 255, 255))

        # # keep bunny facing forward
        global frame
        frame += 1
        if debug and frame % 100 == 0:
            print(self.heading, np.cos(np.radians(self.heading)))
        if np.cos(np.radians(self.heading)) >= 0:
            self.img = pygame.transform.rotate(self.img_right, self.heading + 90)
        else:
            self.img = pygame.transform.rotate(self.img_left, self.heading - 90)

        rect = self.img.get_rect()
        rect.center = int(self.x), int(self.y)
        self.screen.blit(self.img, rect)

        # Update the display
        pygame.display.flip()

        # Cap the frame rate to 60 FPS
        self.clock.tick(self.fps)

    def exit(self):
        print("Exiting simulation")
        self.running = False
        pygame.display.quit()
        pygame.quit()
        sys.exit()
        
    def start_simulation(self):
        # Initialize the Pygame window
        pygame.init()
        self.screen = pygame.display.set_mode((self.box_width, self.box_height))
        pygame.display.set_caption("Robot Simulator")
        self.render()

# # Real Robot Driver
# class RealRobotDriver:
#     def __init__(self):
        
#         #GPIO Mode (BOARD / BCM)
#         GPIO.setmode(GPIO.BCM)

#         #set GPIO Pins for Sonar Sensors
#         self.GPIO_LEFT_TRIGGER = 5
#         self.GPIO_LEFT_ECHO = 6
#         self.GPIO_RIGHT_TRIGGER = 17
#         self.GPIO_RIGHT_ECHO = 27

#         # set GPIO pins for motors
#         self.GPIO_LEFT_MOTOR_SPEED = 12
#         self.GPIO_LEFT_MOTOR_BLUE = 1
#         self.GPIO_LEFT_MOTOR_ORANGE = 7
#         self.GPIO_RIGHT_MOTOR_SPEED = 18
#         self.GPIO_RIGHT_MOTOR_BLUE = 24
#         self.GPIO_RIGHT_MOTOR_ORANGE = 23

#         #set GPIO direction (IN / OUT)
#         GPIO.setup(self.GPIO_LEFT_TRIGGER, GPIO.OUT)
#         GPIO.setup(self.GPIO_LEFT_ECHO, GPIO.IN)
#         GPIO.setup(self.GPIO_RIGHT_TRIGGER, GPIO.OUT)
#         GPIO.setup(self.GPIO_RIGHT_ECHO, GPIO.IN)

#         GPIO.setup(self.GPIO_LEFT_MOTOR_SPEED, GPIO.OUT)
#         GPIO.setup(self.GPIO_LEFT_MOTOR_BLUE, GPIO.OUT)
#         GPIO.setup(self.GPIO_LEFT_MOTOR_ORANGE, GPIO.OUT)
#         GPIO.setup(self.GPIO_RIGHT_MOTOR_SPEED, GPIO.OUT)
#         GPIO.setup(self.GPIO_RIGHT_MOTOR_BLUE, GPIO.OUT)
#         GPIO.setup(self.GPIO_RIGHT_MOTOR_ORANGE, GPIO.OUT)

#     def sonars(self):
#         left_distance = self.sonar(self.GPIO_LEFT_TRIGGER, self.GPIO_LEFT_ECHO)
#         right_distance = self.sonar(self.GPIO_RIGHT_TRIGGER, self.GPIO_RIGHT_ECHO)
#         return left_distance, right_distance

#     def sonar(self, GPIO_TRIGGER, GPIO_ECHO):
#         # set Trigger to HIGH
#         GPIO.output(GPIO_TRIGGER, True)

#         # set Trigger after 0.01ms to LOW
#         time.sleep(0.00001)
#         GPIO.output(GPIO_TRIGGER, False)

#         StartTime = time.time()
#         StopTime = time.time()

#         # save StartTime
#         while GPIO.input(GPIO_ECHO) == 0:
#             StartTime = time.time()

#         # save time of arrival
#         while GPIO.input(GPIO_ECHO) == 1:
#             StopTime = time.time()

#         # time difference between start and arrival
#         TimeElapsed = StopTime - StartTime
#         # multiply with the sonic speed (34300 cm/s)
#         # and divide by 2, because there and back
#         distance = (TimeElapsed * 34300) / 2

#         return distance
    
#     def stop(self):
#         GPIO.output(self.GPIO_LEFT_MOTOR_BLUE, GPIO.LOW)
#         GPIO.output(self.GPIO_LEFT_MOTOR_ORANGE, GPIO.LOW)
#         GPIO.output(self.GPIO_LEFT_MOTOR_SPEED, GPIO.LOW)
#         GPIO.output(self.GPIO_RIGHT_MOTOR_BLUE, GPIO.LOW)
#         GPIO.output(self.GPIO_RIGHT_MOTOR_ORANGE, GPIO.LOW)
#         GPIO.output(self.GPIO_RIGHT_MOTOR_SPEED, GPIO.LOW)
#         GPIO.output(self.GPIO_LEFT_TRIGGER, GPIO.LOW)
#         GPIO.output(self.GPIO_RIGHT_TRIGGER, GPIO.LOW)

#     def motor(self, velocity, speed_pin, blue_pin, orange_pin):
#         if velocity == 0:
#             GPIO.output(blue_pin, GPIO.LOW)
#             GPIO.output(orange_pin, GPIO.LOW)
#             GPIO.output(speed_pin, GPIO.LOW)
#         elif velocity > 0:
#             GPIO.output(blue_pin, GPIO.HIGH)
#             GPIO.output(orange_pin, GPIO.LOW)
#             GPIO.output(speed_pin, GPIO.HIGH)
#         else:
#             GPIO.output(blue_pin, GPIO.LOW)
#             GPIO.output(orange_pin, GPIO.HIGH)
#             GPIO.output(speed_pin, GPIO.HIGH)
    
#     def motors(self, left, right, seconds):
#         # Call real robot hardware control for left motor
#         #self.robot_hardware.set_left_motor_speed(left)
#         #self.robot_hardware.set_right_motor_speed(right)
#         self.motor(left, self.GPIO_LEFT_MOTOR_SPEED, self.GPIO_LEFT_MOTOR_BLUE, self.GPIO_LEFT_MOTOR_ORANGE)
#         self.motor(right, self.GPIO_RIGHT_MOTOR_SPEED, self.GPIO_RIGHT_MOTOR_BLUE, self.GPIO_RIGHT_MOTOR_ORANGE)
#         time.sleep(seconds)
#         self.stop()

#     def exit(self):
#         self.stop()
#         return
