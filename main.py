# Import the robot control commands from the library
from challengebot import Robot
import time

robot = Robot(use_simulator=False)
print("Robot simulation started!")

def forward(x):
    robot.motors(1, 1, x)

def right(x):
    robot.motors(1, -1, x)

def left(x):
    robot.motors(-1, 1, x)

def dance():
    right(5)
    left(5)
    forward(5)

# Main student program
while True:
    # Get input from the user
    command = input("Enter command (f/l/r/stop/exit/dance): ")

    if command == "f":
        forward(0.1)
    elif command == "l":
        left(0.1)
    elif command == "r":
        right(0.1)
    elif command == "exit":
        break
    elif command == "dance":
        dance()
    else:
        print("Unknown command")

    # Check distance from an obstacle
    print("Distance to object:", robot.sonars())

robot.exit()
