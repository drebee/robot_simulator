# Import the robot control commands from the library
from simulator import robot
import time

def forward(x):
    robot.motors(1, 1, x)

def right(x):
    robot.motors(1, -1, x)

def left(x):
    robot.motors(-1, 1, x)

def back(x):
    robot.motors(-1, -1, x)

def dance():
    right(5)
    forward(10)

# Main student program
while True:
    # Get input from the user
    command = input("Enter command (f/l/r/stop/exit/dance): ")

    if command == "f":
        forward(0.5)
    elif command == "l":
        left(0.5)
    elif command == "r":
        right(0.5)
    elif command == "b":
        back(0.5)
    elif command == "exit":
        break
    elif command == "dance":
        dance()
    else:
        print("Unknown command")

    # Check distance from an obstacle
    print("Distance to object:", robot.sonars())

robot.exit()
