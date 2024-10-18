import pygame
import os
import numpy as np
import sys

import RPi.GPIO as GPIO
import time

frame = 0
debug = False

class Robot:
    def __init__(self, use_simulator=True):
        if use_simulator:
            self.driver = SimulatorDriver()

        else:
            self.driver = RealRobotDriver()  # driver can be a simulator or real robot

    def motors(self, left, right, seconds):
        self.driver.motors(left, right, seconds)
    
    def sonars(self):
        return self.driver.sonars()
    
    def exit(self):
        self.driver.exit()

# Simulator Driver
class SimulatorDriver:
    def __init__(self):
        self.x = 300  # Starting x position
        self.y = 200  # Starting y position
        self.heading = 0 # pointing to the right
        self.left_motor_velocity = 0
        self.right_motor_velocity = 0
        self.radius = 20  # Robot radius for visualization
        size = 100
        self.img_left = pygame.image.load(os.path.join('img', "left", f"{size}", 'robobunny.png'))
        self.img_right = pygame.image.load(os.path.join('img', "right", f"{size}", 'robobunny.png'))
        self.img = self.img_left
        self.running = True
        self.clock = pygame.time.Clock()
        self.fps = 60

        self.start_simulation()

    def motors(self, left, right, seconds):
        # power (+ / -) to left and right motors
        # number of seconds to maintain that

        # for a certain number of seconds:
        for _ in range(seconds * self.fps):
            # update position
            if right == 1 and left == -1:
                self.heading = (self.heading - 1) % 360
            elif right == -1 and left == 1:
                self.heading = (self.heading + 1) % 360
            elif right == left:
                if right == 0:
                    pass
                else:
                    speed = right * 1
                    self.x += speed * np.cos(np.radians(self.heading))
                    self.y -= speed * np.sin(np.radians(self.heading))

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
        self.screen = pygame.display.set_mode((600, 400))
        pygame.display.set_caption("Robot Simulator")

# Real Robot Driver
class RealRobotDriver:
    def __init__(self):
        
        #GPIO Mode (BOARD / BCM)
        GPIO.setmode(GPIO.BCM)

        #set GPIO Pins
        self.GPIO_LEFT_TRIGGER = 5
        self.GPIO_LEFT_ECHO = 6
        self.GPIO_RIGHT_TRIGGER = 17
        self.GPIO_RIGHT_ECHO = 27

        #set GPIO direction (IN / OUT)
        GPIO.setup(self.GPIO_LEFT_TRIGGER, GPIO.OUT)
        GPIO.setup(self.GPIO_LEFT_ECHO, GPIO.IN)
        GPIO.setup(self.GPIO_RIGHT_TRIGGER, GPIO.OUT)
        GPIO.setup(self.GPIO_RIGHT_ECHO, GPIO.IN)

    def sonars(self):
        left_distance = self.sonar(self.GPIO_LEFT_TRIGGER, self.GPIO_LEFT_ECHO)
        right_distance = self.sonar(self.GPIO_RIGHT_TRIGGER, self.GPIO_RIGHT_ECHO)
        return left_distance, right_distance

    def sonar(self, GPIO_TRIGGER, GPIO_ECHO):
        # set Trigger to HIGH
        GPIO.output(GPIO_TRIGGER, True)

        # set Trigger after 0.01ms to LOW
        time.sleep(0.00001)
        GPIO.output(GPIO_TRIGGER, False)

        StartTime = time.time()
        StopTime = time.time()

        # save StartTime
        while GPIO.input(GPIO_ECHO) == 0:
            StartTime = time.time()

        # save time of arrival
        while GPIO.input(GPIO_ECHO) == 1:
            StopTime = time.time()

        # time difference between start and arrival
        TimeElapsed = StopTime - StartTime
        # multiply with the sonic speed (34300 cm/s)
        # and divide by 2, because there and back
        distance = (TimeElapsed * 34300) / 2

        return distance
    
    def motors(self, left, right, seconds):
        # Call real robot hardware control for left motor
        #self.robot_hardware.set_left_motor_speed(left)
        #self.robot_hardware.set_right_motor_speed(right)
        pass

    def exit(self):
        return
