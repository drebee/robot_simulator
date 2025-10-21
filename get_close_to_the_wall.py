# Import the robot control commands from the library
from simulator import robot
import time

#screen size = 660, 410
#robot 200 pixels by 200 pixels
#starting screen size with robot
    #460 to left/right wall
    #153.72475374938272 to up/down wall

#speed 120.57 pixles per second
    # exactly  120.56843196030017 pixels per second 
#turning speed 59.8 degrees per second
    #58.8 degrees per second.







def lefturn(degrees):
    degrees = degrees/58.8
    robot.motors(1, -1, degrees)

def rightturn(degrees):
    degrees = degrees/58.8
    robot.motors(-1, 1, degrees)

def turn180():
    robot.motors(1, 1, (1.5319148936170213*2))

def left90():
    robot.motors(1, -1, 1.5319148936170213)

def right90():
    robot.motors(-1, 1, 90/58.8)
    
def start_right_wall():
        robot.motors(1,1,3.8416)

def start_left_wall():
        robot.motors(1,1,3.3416)

def reverseright():
    robot.motors(-1, -1, 3.8416)

def reverseup():
    robot.motors(-1, -1, 1.275)


def start_up_wall():
    robot.motors(1, 1, 1.275)

def forward_to_wall():
    close_dist = 3
    while robot.left_sonar() > close_dist and robot.right_sonar() > close_dist:
        robot.motors(1, 1, 0.5)

def closewall():
    print("first, let's get really close to the walls!")
    wall = input("which wall do you want to get really close to? (right, left, up, down), or if you want to end, say end\n")
    if wall == "right":
        forward_to_wall()
        print("")
        reverseright()
    elif wall == "left":
        print("hi")
        rightturn(90)
        rightturn(90)
        forward_to_wall()
        print("ha did not crash")
        reverseright()
        left90()
        left90()
    elif wall == "up":
        left90()
        forward_to_wall()
        # print("erm this is actually 153.72475374938272 pixles")
        reverseup()
        right90()
    elif wall == "down":
        print("right 90")
        right90()
        print("forward to wall")
        forward_to_wall()
        print("reverse up")
        reverseup()
        print("left 90")
        left90() 
    elif wall == "end":
        print("glad you had fun")
        print("alright now that we have given Dr. Eb a heart attack (and me beacuse IDK IF THIS WILL WORK) lets do some reall fun stuff")
        return
    else:
        print("please tell me left, right, up, or down or end. ")
        closewall()
    while wall in ["right", "left", "up", "down"]:
        closewall()

def bounceuselesss(): 


    lefturn(45)
    bounces = input("how many times do you want to bounce for")
    bounces = int(bounces)
        
    if bounces >= 20:
        pass
    else:
        print("ok, you messed up, now its time to restart")
        return bounceuselesss()
   
    for i in range(1000):
        if bounces == 0:
            break
        else:
            pass
        for i in range(bounces):        
            left = robot.left_sonar()
            right = robot.right_sonar() 
            # left, right = robot.sonars()
            # print(left)
            ftime = left/130
            if ftime>=4:
                robot.motors(-1, -1, 1)
                left = robot.left_sonar()
                right = robot.right_sonar() 
                if left>right:
                    left90()
                    bounces = bounces-1
                    break
                elif right>left:
                    right90()
                    bounces = bounces-1
                    break
                else:
                    return limbo()   
            elif ftime >= 2.5:
                print("issue")
                ftime = 1.5
                robot.motors(-1, -1, ftime)
            if ftime <= 0.5:
                robot.motors(-1, -1, 1)
                left = robot.left_sonar()
                right = robot.right_sonar() 
                if left>right:
                    left90()
                    bounces = bounces-1
                    break
                elif right>left:
                    right90()
                    bounces = bounces-1
                    break
                else:
                    return limbo()   
            else:
                print("this should work")
                print(ftime)
                ftime = ftime-0.5
                robot.motors(1, 1, ftime)
                
                    
                lefturn(90)


def limbo():
    print("wow, nick really did not want to figure out how to fix this for every possible orintation, so beacuse of that, enjoy this")
    for i in range(50):
        turn180()
        print("insert clown music")






def bounce2():
    
    input("say anything to start")
    lefturn(45)
    bounces = 2
    bounces = int(bounces)
    for i in range(2):
        for i in range(bounces):
            left = robot.left_sonar()
            right = robot.right_sonar() 
            timeleft = left/150
            print(timeleft)
            timeright = right/150
            print(timeright)
            if timeleft>timeright:
                ftime = timeright
                print("right")
            elif timeright>timeleft:
                print("left")
                ftime = timeleft
            else:
                print("Nick, Dr Eb, or anybody else who comes across this, how did this happen.")
            print(ftime)



            if ftime >= 0.9 and ftime <=1000:
                #print("lost of pain here")
                robot.motors(-1, -1 ,1)
            elif ftime <= 0.5:
                #print("0.5")
                robot.motors(-1, -1, 1)
            else:
                #print("else")

                robot.motors(1, 1, ftime)

            if ftime == timeright:
                right90()
            elif ftime == timeleft:
                left90()
            else:
                robot.motors(-1, -1, 1)
    rightturn(45)
        

        
closewall()
bounce2()























