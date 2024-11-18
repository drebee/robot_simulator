# Import the robot control commands from the library
from simulator import robot
import time

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
        forward(1)
    elif command == "l":
        left(1)
    elif command == "r":
        right(1)
    elif command == "exit":
        break
    elif command == "dance":
        dance()
    else:
        print("Unknown command")

    # Check distance from an obstacle
    print("Distance to object:", robot.sonars())

robot.exit()
