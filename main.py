# Import the robot control commands from the library
from challengebot import Robot
import time

robot = Robot(use_simulator=True)
print("Robot simulation started!")

def stop():
    robot.left_motor(0)
    robot.right_motor(0)

def forward(x):
    robot.right_motor(1)
    robot.left_motor(1)
    time.sleep(x)
    stop()

def right(x):
    robot.right_motor(1)
    robot.left_motor(-1)
    time.sleep(x)
    stop()

def left(x):
    robot.right_motor(-1)
    robot.left_motor(1)
    time.sleep(x)
    stop()

def dance():
    right(0.5)
    left(0.5)
    forward(0.5)

# Main student program
while True:
    # Get input from the user
    command = input("Enter command (forward/left/right/stop): ")

    if command == "f":
        forward(1)
    elif command == "l":
        left(1)
    elif command == "r":
        right(1)
    elif command == "stop":
        stop()
    elif command == "exit":
        break
    elif command == "dance":
        dance()
    else:
        print("Unknown command")

    # Check distance from an obstacle
    print("Distance to object:", robot.distance())
