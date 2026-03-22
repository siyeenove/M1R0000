# Imports go at the top
from microbit import *

# Read the battery level
# 4 AA batteries
def readBatteryLevel():
    # Read the battery voltage value
    batLevel = pin2.read_analog()
    if batLevel > 310:   # 310=6V/6/0.0032226, 100%
            batLevel = 310    
    if batLevel < 232:   # 232=4.5V/6/0.0032226, 0%
            batLevel = 232
    # Map 232-310 values to 0-100
    batLevel = scale(batLevel, from_=(232, 310), to=(0, 100))
    return batLevel  # return battery level
        
# Code in a 'while True:' loop repeats forever
while True:       
    # Dot matrix display of battery level
    display.show(readBatteryLevel())
    sleep(1000)  # delay 1000 milliseconds
