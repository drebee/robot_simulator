# Import the robot control commands from the library
from simulator import robot
from time import *

degree = 0

def spin(spin_direction, spin_duration):
    global degree
    if spin_direction == "r" or spin_direction == "R" or spin_direction == "right" or spin_direction == "Right":
        robot.motors(-1, 1, spin_duration)
        degree = (degree-(spin_duration*58.8))%360
    if spin_direction == "l" or spin_direction == "L" or spin_direction == "left" or spin_direction == "Left":
        robot.motors(1,-1, spin_duration)
        degree = (degree+(spin_duration*58.8))%360

def turn90():
    global degree
    turn_direction = input("do you want to turn left (L) or right (R)? ")
    if turn_direction == "r" or turn_direction == "R" or turn_direction == "right" or turn_direction == "Right":
        robot.motors(-1, 1, (90/58.8))
        degree = (degree-90)%360
    if turn_direction == "l" or turn_direction == "L:" or turn_direction == "left" or turn_direction == "Left":
        robot.motors(1, -1, (90/58.8))
        degree = (degree+90)%360

def dance():
    global degree
    dancing = float(input("how many dance loops do you want me to do (one loop is 10 seconds)? "))
    beat = 0.5
    while dancing > 0:
        robot.motors(-1,1,beat)
        robot.motors(1,-1,beat*2)
        robot.motors(-1,1,beat)
        robot.motors(1,1,beat)
        robot.motors(-1,-1,beat*2)
        robot.motors(1,1,beat)
        robot.motors(1,-1,beat)
        robot.motors(-1,1,beat*2)
        robot.motors(1,-1,beat)
        robot.motors(-1,-1,beat)
        robot.motors(1,1,beat*2)
        robot.motors(-1,-1,beat)
        robot.motors(-1,1,beat)
        robot.motors(1,-1,beat*2)
        robot.motors(-1,1,beat)
        dancing-=1
        degree = degree%360

def drive():
    global degree
    drive_duration = float(input("how long do you want to drive for? "))
    l = 1
    r = 1
    def forward_drive(drive_duration):
        global degree
        remainder = drive_duration
        left = robot.left_sonar()
        right = robot.right_sonar()
        if left<3 or right<3:
            robot.motors(-r, l, 3.06)
            remainder = remainder-0.1
            degree = (degree+180)%360
            if remainder <0.1:
                return
            forward_drive(remainder)
        else:
            robot.motors(r, l, 0.1)
            remainder = remainder-0.1
            if remainder <0.1:
                return
            forward_drive(remainder)

    forward_drive(drive_duration)

def center():
    global degree
    if (degree%360)<=180:
        robot.motors(-1, 1, (degree)/58.8)
    if degree%360>180:
        robot.motors(1,-1, 180-(degree-180))
    #og sensor reading is 90
    og_dist = 90
    left = robot.left_sonar()
    right = robot.right_sonar()
    if left<=og_dist or right<=og_dist:
        robot.motors(-1,-1, og_dist-left)
    if left>og_dist or right>og_dist:
        robot.motors(1,1, left-og_dist)

def stay():
    global degree
    stay_in_place = float(input("How long do you want to stay for? "))
    robot.motors(0,0,stay_in_place)
    degree = (degree)%360
    move()

def move():
    global degree
    hi = input("Hi! I'm robobunny. What would you like me to do? I can spin, turn90, dance(before you run this, make sure you are in the middle of the box), drive, or stay \n")

    if hi == str("spin"):
        spin_direction = input("do you want to spin left (L) or right (R)? ")
        spin_duration = float(input("how long do you want to spin for? "))
        spin(spin_direction,spin_duration)
    elif hi == str("turn90"):
        turn90()
    elif hi == str("dance"):
        dance()
    elif hi == str("drive"):
        drive()
    elif hi == str("stay"):
        stay()
    elif hi == str("center"):
        center()
    else:
        print("Sorry, I don't know how to do that. Please try again")
    move()
       
move()
