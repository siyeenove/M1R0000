# Imports go at the top
from microbit import *

# Define the pins of the joystick
x_axis = pin1
y_axis = pin0

# Read the joystick value function
def readJoystickValue(axis):
    # Map the values from 0 to 1023 to -100 to +100,
    # and then return the mapped value
    return scale(axis.read_analog(), from_=(0, 1023), to=(-100, 100))

# Code in a 'while True:' loop repeats forever
while True:
    # Determine whether the value of the X-axis is greater than 80
    if readJoystickValue(x_axis) > 80:  
        # Dot matrix displays character 'L'
        display.show('L')

    # Determine whether the value of the X-axis is  less than -80
    if readJoystickValue(x_axis) < -80: 
        # Dot matrix displays character 'R'
        display.show('R')

    # Determine whether the value of the Y-axis is  greater than 80
    if readJoystickValue(y_axis) > 80:  
        # Dot matrix displays character 'U'
        display.show('U')

    # Determine whether the value of the Y-axis is  less than -80
    if readJoystickValue(y_axis) < -80: 
        # Dot matrix displays character 'D'
        display.show('D')

    # delay 100 millisecond
    sleep(100)
