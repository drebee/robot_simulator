import pygame
import threading
import time
import os
import numpy as np
import sys

frame = 0
debug = False

class Robot:
    def __init__(self, use_simulator=True):
        if use_simulator:
            self.driver = SimulatorDriver()

        else:
            self.driver = RealRobotDriver()  # driver can be a simulator or real robot
    
    def left_motor(self, velocity):
        self.driver.left_motor(velocity)
    
    def right_motor(self, velocity):
        self.driver.right_motor(velocity)
    
    def distance(self):
        return self.driver.distance()
    
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

        self.start_simulation()
    
    def left_motor(self, velocity):
        self.left_motor_velocity = velocity
    
    def right_motor(self, velocity):
        self.right_motor_velocity = velocity
    
    def distance(self):
        return 10

    def update(self):
        # Basic update logic for robot movement based on motor velocities
        # You can refine this to simulate more accurate movement
        if self.right_motor_velocity == 1 and self.left_motor_velocity == -1:
            self.heading = (self.heading - 1) % 360
        elif self.right_motor_velocity == -1 and self.left_motor_velocity == 1:
            self.heading = (self.heading + 1) % 360
        elif self.right_motor_velocity == self.left_motor_velocity:
            if self.right_motor_velocity != 0:
                # go forward in direction of heading
                speed = self.right_motor_velocity * 1
                self.x += speed * np.cos(np.radians(self.heading))
                self.y -= speed * np.sin(np.radians(self.heading))

    def render(self, screen):
        # Clear the screen
        screen.fill((255, 255, 255))

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
        screen.blit(self.img, rect)

        # Update the display
        pygame.display.flip()
    
    def run_simulation(self):
        # Start the Pygame rendering loop
        clock = pygame.time.Clock()
        while self.running:
            
            # Update the robot state
            self.update()

            # Render the robot in the window
            self.render(self.screen)

            # Cap the frame rate to 60 FPS
            clock.tick(60)

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

        # Start the simulation in a separate thread or process
        threading.Thread(target=self.run_simulation, daemon=True).start()

# Real Robot Driver
class RealRobotDriver:
    def __init__(self, robot_hardware):
        self.robot_hardware = robot_hardware
    
    def left_motor(self, velocity):
        # Call real robot hardware control for left motor
        self.robot_hardware.set_left_motor_speed(velocity)
    
    def right_motor(self, velocity):
        # Call real robot hardware control for right motor
        self.robot_hardware.set_right_motor_speed(velocity)
    
    def distance(self):
        # Get distance from real robot sensor
        return self.robot_hardware.get_sonar_distance()

# Control functions can be called from the student code now
