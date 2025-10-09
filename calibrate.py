from simulator import robot, FORWARD, BACKWARD, STOP

while True:
    command = input("Motor (m) or Sonars (s) or Quit (q)? ")
    if command == "m":
        left_power = int(input("Left motor: "))
        right_power = int(input("Right motor: "))
        seconds = int(input("Seconds: "))

        robot.motors(left = left_power, right = right_power, seconds = seconds)

    elif command == "s":
        print("Left: ", robot.left_sonar())
        print("Right: ", robot.right_sonar())

    elif command == "q":
        robot.exit()
        break

