import pygame
import os
import numpy as np
import sys
import time

frame = 0
debug = False

class Robot:
    def __init__(self, use_simulator = True):
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
            else:
                raise Exception("Ooops! Dr. Ebee didn't write code that let's you use those numbers as input to the `motors` function. If you *really* want those numbers, schedule some time on her calendar to help her implement that change!!")

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

mode = input("Do you want to run the real robot (r) or the simulator (s)?")
if mode == "r":
    from robot import RealRobotDriver
    robot = Robot(use_simulator=False)
    print("Robot simulation started!")
else:
    robot = Robot(use_simulator=True)
    print("Robot simulation started!")