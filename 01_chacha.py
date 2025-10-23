# Import the robot control commands from the library
from simulator import robot
import time

#660x440

def stomp(direction):
    if direction== "right":
        # 1.5 seconds
        robot.motors(1, -1, 0.5)
        robot.motors(1,1,0.25)
        robot.motors(-1,-1,0.25)
        robot.motors(1,1,0.25)
        robot.motors(-1,-1,0.25)
        robot.motors(-1,1,0.5)
    if direction== "left":
        # 1.5 seconds
        robot.motors(-1, 1, 0.5)
        robot.motors(1,1,0.25)
        robot.motors(-1,-1,0.25)
        robot.motors(1,1,0.25)
        robot.motors(-1,-1,0.25)
        robot.motors(1,-1,0.5)

def slide(direction):
    if direction== "right":
        robot.motors(1, -1, 1.52)
        robot.motors(1,1,0.5)
        robot.motors(-1,-1,0.5)
        robot.motors(-1,1,1.52)
    if direction== "left":
        # 1.5 second
        robot.motors(-1, 1, 1.52)
        robot.motors(1,1,0.5)
        # robot.motors(-1,-1,0.25)
        # robot.motors(1,-1,.25)

def backnowyall():
    # 2 seconds
    robot.motors(1,-1,1.52)
    robot.motors(-1,-1,.75)
    # time.sleep(0.25)
    # robot.motors(1,1,0.5)

def hop():
    # .5 second
    robot.motors(1,1,0.125)
    robot.motors(-1,-1,0.125)
    

def knees():
    # 3 seconds
    robot.motors(-1, 1, 0.2)
    robot.motors(1,1,0.2)
    robot.motors(-1,-1,0.2)
    robot.motors(1, -1, 0.2)
    robot.motors(1,1,0.2)
    robot.motors(-1,-1,0.2)
    robot.motors(-1, 1, 0.2)
    robot.motors(1,1,0.2)
    robot.motors(-1,-1,0.2)
    robot.motors(1, -1, 0.2)
    robot.motors(1,1,0.2)
    robot.motors(-1,-1,0.2)
    robot.motors(-1, 1, 0.2)
    robot.motors(1,1,0.2)
    robot.motors(-1,-1,0.2)
    robot.motors(1, -1, 0.2)

def getfunkywithit():
    robot.motors(1,1,0.5)
    robot.motors(1,-1,1.5)

def chacha():
    robot.motors(1,1,1.5)
    left_distance = robot.left_sonar()
    right_distance = robot.right_sonar()
    robot.motors(1,1,1.5)
    left_distance = robot.left_sonar()
    right_distance = robot.right_sonar()
    robot.motors(-1,-1,1.5)
    left_distance = robot.left_sonar()
    right_distance = robot.right_sonar()
    robot.motors(-1,1,2)
    robot.motors(1,-1,2)
    if left_distance <5 and right_distance <5:
        robot.motors(-1,-1,0.5)  

        left_distance = robot.left_sonar()
        right_distance = robot.right_sonar() 
    if right_distance <5:
        robot.motors(-1,-1,0.5)
    robot.motors(-1,1,0.1)
    left_distance = robot.left_sonar()
    right_distance = robot.right_sonar()  
    if left_distance <5 and right_distance <5:
        robot.motors(-1,-1,0.5) 
    left_distance = robot.left_sonar()
    right_distance = robot.right_sonar()
    if right_distance <5:
        robot.motors(-1,-1,0.5)
    robot.motors(1,-1,1)
    left_distance = robot.left_sonar()
    right_distance = robot.right_sonar()
    if left_distance <5 and right_distance <5:
        robot.motors(-1,-1,0.5)  
    left_distance = robot.left_sonar()
    right_distance = robot.right_sonar()
    if right_distance <5:
        robot.motors(-1,-1,0.5)

def drebee(c):
    return "thanks for being an awesome teacher," +c +"! you've been the sweetest and genuinely make me excited to learn. let me know if you ever need to talk. i'm always here for you!! hope you have a great holiday break!"

def hello(b):
    return "hi "+b +"!"

# p =input("are you ready to cha cha?")
# o=input("are you sure?")
# oo=input("is it time to get funky?")
# ooo=input("is it really time to get funky?")


robot.motors(-1, 1, 1.52)
for i in range(3):
    print(f"{3-i}...")
    time.sleep(1)
print("Cha Cha!!!")
print()
time.sleep(1.5)
print("To the left...")
slide("left")
print("Take it back now, y'all...")
backnowyall()
print("Two hops this time...")
time.sleep(1)
hop()
hop()
print("Two hops this time...")
time.sleep(1)
hop()
hop()
print("Right foot two stomps...")
stomp("right")
print("Left foot two stomps...")
stomp("left")
print("Hands on your knees...")
knees() 
print("Get funky with it...")
getfunkywithit()
print("Cha cha...")
chacha()
