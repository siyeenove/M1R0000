# Imports go at the top
from microbit import *

# Define the pins of the A, B, C, and D button
button_a = pin5
button_b = pin11
button_c = pin12
button_d = pin8

# I/O port with pull resistor
button_a.set_pull(button_a.PULL_UP)
button_b.set_pull(button_b.PULL_UP)
button_c.set_pull(button_c.PULL_UP)
button_d.set_pull(button_d.PULL_UP)

# Read button value function
def readButtonValue(button):
    # Return button value
    return button.read_digital()

# Code in a 'while True:' loop repeats forever
while True:
    # Determine whether button_a is pressed
    if readButtonValue(button_a) == 0:
        # If button_a is pressed, dot matrix displays character 'A'
        display.show('A') 
        
    # Determine whether button_b is pressed
    if readButtonValue(button_b) == 0:
        # If button_b is pressed, dot matrix displays character 'B'
        display.show('B')
        
    # Determine whether button_c is pressed
    if readButtonValue(button_c) == 0:
        # If button_c is pressed, dot matrix displays character 'C'
        display.show('C')
        
    # Determine whether button_d is pressed
    if readButtonValue(button_d) == 0:
        # If button_d is pressed, dot matrix displays character 'D'
        display.show('D')
        
    # delay 100 millisecond
    sleep(100)
