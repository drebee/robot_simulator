To install all dependencies, type the following into the Terminal (if you're on Mac) or Anaconda prompt (if you're on Windows):

    conda activate cs2526
    pip install pygame
    conda install numpy

Project Requirements:
* [ ] robot moves
* [ ] robot does not crash into the walls of the box
* [ ] at least 5 calls to input
* [ ] at least 5 functions
* [ ] at least 2 functions have at least one parameter
* [ ] at least 2 functions have return values and at least one call to the function is assigned to a variable
* [ ] each motor moves at least once
* [ ] the robot's movement changes based on at least 5 readings of the sonar sensors
* [ ] use at least 1 while loop OR recursive function call
* [ ] at least one command (user input) causes the robot to move autonomously for at least 20 seconds

Dr. EB Todo:
* [ ] add noise to simulator motors and sonars

Wiring:

Pi - HDMI side long row from ethernet to SD card:
* ground
* blank x3
* pin 6 = left trigger
* pin 5 = left echo
* blank x7
* pin 27 = right echo
* pin 17 = right trigger
* blank x5

Pi - NON-HDMI side long row from ethernet to SD card:
* blank x4
* pin 12 = left speed (white)
* blank
* pin 1 = left forward (blue)
* pin 7 = left backward (orange)
* blank x3
* pin 24 = right forward (blue)
* pin 23 = right backward (orange)
* blank
* pin 18 = right speed (white)
* blank x4
* 5v = power line of breadboard

Breadboard - left motor, left of caterpillar if indent is on top, from top to bottom:
* white
* yellow
* ground
* ground
* orange
* battery power

Breadboard - right motor, right of caterpillar if indent is on top, from top to bottom:
* power from pi
* blue
* green
* ground
* ground
* yellow
* orange
* white
