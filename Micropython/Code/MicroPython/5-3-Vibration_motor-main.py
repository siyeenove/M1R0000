# Imports go at the top
from microbit import *

# Define the vibration motor state variables
ON = 1
OFF = 0

# Control the vibration motor function
def setVibrationMotor(OnOrOff):
    # Determine whether the value of the variable OnOrOff is equal to 1
    if OnOrOff == ON:  
        # Turn on the vibration motor
        pin2.write_digital(1)
    # Determine whether the value of the variable OnOrOff is equal to 0
    if OnOrOff == OFF:   
        # Turn off the vibration motor
        pin2.write_digital(0)

# Code in a 'while True:' loop repeats forever
while True:
    # Turn on the vibration motor
    setVibrationMotor(ON)
    sleep(1000)  # delay 1000 millisecond
    
    # Turn off the vibration motor
    setVibrationMotor(OFF)
    sleep(1000)  # delay 1000 millisecond
