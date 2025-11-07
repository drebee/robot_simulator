from simulator import robot, FORWARD, BACKWARD, STOP

# TODO: Write your code here!
# Use robot.motors() to move
# Use robot.left_sonar() and robot.right_sonar() to sense obstacles

left_distance_in_cm = robot.left_sonar()
print(left_distance_in_cm)

robot.motors(left = FORWARD, right = FORWARD, seconds = 20)

# When you're done, close the simulator
robot.exit()