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

## Wiring Documentation

### Raspberry Pi GPIO Connections

![pi_pins.png](pi_pins.jpg)

**Sonar Sensors (HC-SR04):**
- Pin 6 (GPIO 6) → Left Trigger
- Pin 5 (GPIO 5) → Left Echo
- Pin 17 (GPIO 17) → Right Trigger
- Pin 27 (GPIO 27) → Right Echo

**Motor Controller (L298N):**
- Pin 12 (GPIO 12/PWM0) → Left Motor Speed (white wire)
- Pin 1 (GPIO 1) → Left Motor Forward (blue wire)
- Pin 7 (GPIO 7) → Left Motor Backward (orange wire)
- Pin 18 (GPIO 18/PWM0) → Right Motor Speed (white wire)
- Pin 24 (GPIO 24) → Right Motor Forward (blue wire)
- Pin 23 (GPIO 23) → Right Motor Backward (orange wire)

**Power:**
- 5V pin → Breadboard power rail

### Physical Pin Layout
*Looking at Pi with HDMI ports on left, SD card on right, from ethernet to SD card:*

**Top row (away from HDMI):**
Ground, blank x3, pin 6 (left trigger), pin 5 (left echo), blank x7, pin 27 (right echo), pin 17 (right trigger), blank x5

**Bottom row (near HDMI):**
Blank x4, pin 12 (left speed/white), blank, pin 1 (left forward/blue), pin 7 (left backward/orange), blank x3, pin 24 (right forward/blue), pin 23 (right backward/orange), blank, pin 18 (right speed/white), blank x4, 5V (power to breadboard)

### Motor Controller Breadboard Connections

![motor_controller_sn754410.jpg](motor_controller_sn754410.jpg)

**Left Motor** (left side when viewing caterpillar track indent from top):
1. White (from Pi pin 12 - speed control)
2. Yellow (motor wire)
3. Ground
4. Ground
5. Orange (from Pi pin 7 - backward)
6. Battery power

**Right Motor** (right side when viewing caterpillar track indent from top):
1. 5V from Pi
2. Blue (from Pi pin 24 - forward)
3. Green (motor wire)
4. Ground
5. Ground
6. Yellow (motor wire)
7. Orange (from Pi pin 23 - backward)
8. White (from Pi pin 18 - speed control)
