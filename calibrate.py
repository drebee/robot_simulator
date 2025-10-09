from simulator import Robot, FORWARD, BACKWARD, STOP

# Create your robot
robot = Robot(use_simulator=True)

while True:
    left_power = input("Left motor: ")
    right_power = input("Right motor: ")
    seconds = input("Seconds: ")

    robot.motors(left = left_power, right = right_power, seconds = seconds)

# When you're done, close the simulator
robot.exit()