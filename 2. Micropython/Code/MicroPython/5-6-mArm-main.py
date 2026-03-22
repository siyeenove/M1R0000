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

# Read key value function
def readButtonValue(button):
    return button.read_digital()

# Define the pins of the joystick
x_axis = pin1
y_axis = pin0

# Read the joystick value function
def readJoystickValue(axis):
    # Map 0-1023 values to -100 - +100
    return scale(axis.read_analog(), from_=(0, 1023), to=(-100, 100))

# Define the vibration motor state variables
ON = 1
OFF = 0
# Control the vibration motor function
def setVibrationMotor(OnOrOff):
    if OnOrOff == ON:    # Turn on the vibration motor
        pin2.write_digital(1)
    if OnOrOff == OFF:   # Turn off the vibration motor
        pin2.write_digital(0)

# Read the battery level.
# 4 AA batteries
def readBatteryLevel():
    batLevel = pin2.read_analog()
    if batLevel > 310:   # 310=6V/6/0.0032226, 100%
            batLevel = 310    
    if batLevel < 232:   # 232=4.5V/6/0.0032226, 0%
            batLevel = 232
    # Map 232-310 values to 0-100
    batLevel = scale(batLevel, from_=(232, 310), to=(0, 100))
    return batLevel
    
# Servo class
class Servo:
    def __init__(self, pin):
        self.pin = pin
        # Servo parameters
        self.min_pulse = 500    # Pulse width at 0 degrees (microseconds)
        self.max_pulse = 2400   # Pulse width at 180 degrees (microseconds)
        self.period = 20000     # 20ms period (50Hz)
        self.pin.set_analog_period(20)  # Set period to 20ms
        
    def set_angle(self, angle):
        # Limit angle range
        angle = max(0, min(180, angle))
        
        # Calculate pulse width
        pulse_width = self.min_pulse + (angle / 180) * (self.max_pulse - self.min_pulse)
        
        # Convert to analog value (0-1023)
        analog_value = int((pulse_width / self.period) * 1023)
        
        # Set PWM
        self.pin.write_analog(analog_value)
    
    def set_pulse(self, pulse_width):
        # Set pulse width directly (microseconds)
        self.pin.write_analog(pulse_width)
    
# Show happy face
display.show(Image.HAPPY)
sleep(100)  # delay 100 milliseconds

# Define the Angle variables of the 4 servos
servo1_degree = 90
servo2_degree = 90
servo3_degree = 60
servo4_degree = 90

# Create 4 servo objects and define the pins to use
servo1 = Servo(pin13)
servo2 = Servo(pin14)
servo3 = Servo(pin15)
servo4 = Servo(pin16)

# Initialize the angles of the 4 servos
servo1.set_angle(servo1_degree) # Set the Angle of servo1
sleep(500)   # delay 500 milliseconds
servo2.set_angle(servo2_degree)
sleep(500)
servo3.set_angle(servo3_degree)
sleep(500)
servo4.set_angle(servo4_degree)
sleep(500)

# Reads the current time when the program is running
last_time = running_time()
interval = 5000  # 5000ms
last_ticker = running_time()
ticker = 40000   # 40000ms

# An infinite loop statement.
while True:   
    # Reads the current time when the program is running
    current_time = running_time()
    if current_time - last_time >= interval:
        # Display battery power value
        display.show(readBatteryLevel())
        last_time = current_time

    # Prevent the servo of the claws from overheating
    current_ticker = running_time()
    if current_ticker - last_ticker >= ticker:
        # Turn off the pulse of the servo
        servo4.set_pulse(0)
    
    # Read the value of the joystick X-axis and drive the Angle 
    # of the servo1 according to the value.
    if readJoystickValue(x_axis) > 60 and servo1_degree < 180: 
        servo1_degree = servo1_degree + 1   # Variable increments by 1
        servo1.set_angle(servo1_degree)     # Set the Angle of servo1
        sleep(15)
    if readJoystickValue(x_axis) < -60 and servo1_degree > 0:        
        servo1_degree = servo1_degree - 1   # The variable decrements by 1
        servo1.set_angle(servo1_degree)
        sleep(15)
        
    # Read the value of the joystick Y-axis and drive the Angle 
    # of the servo2 according to the value.
    if readJoystickValue(y_axis) > 60 and servo2_degree < 180:        
        servo2_degree = servo2_degree + 1
        servo2.set_angle(servo2_degree)
        sleep(15)
    if readJoystickValue(y_axis) < -60 and servo2_degree > 0:        
        servo2_degree = servo2_degree - 1
        servo2.set_angle(servo2_degree)
        sleep(15)

    # Read the value of the button_a and drive the Angle 
    # of the servo4 according to the value.
    if readButtonValue(button_a) == 0 and servo4_degree > 5:
        servo4_degree = servo4_degree - 1
        servo4.set_angle(servo4_degree)
        sleep(15)
        last_ticker = current_ticker

    # Read the value of the button_b and drive the Angle 
    # of the servo4 according to the value.
    if readButtonValue(button_b) == 0 and servo4_degree < 180:
        servo4_degree = servo4_degree + 1
        servo4.set_angle(servo4_degree)
        sleep(15)
        last_ticker = current_ticker

    # Read the value of the button_c and drive the Angle 
    # of the servo3 according to the value.
    if readButtonValue(button_c) == 0 and servo3_degree > 0:
        servo3_degree = servo3_degree - 1
        servo3.set_angle(servo3_degree)
        sleep(15)

    # Read the value of the button_d and drive the Angle 
    # of the servo3 according to the value.
    if readButtonValue(button_d) == 0 and servo3_degree < 120:
        servo3_degree = servo3_degree + 1
        servo3.set_angle(servo3_degree)
        sleep(15)

    # Executed when the micro:bit v2 logo is touched.
    # Attention! Not compatible with microbit v1.
    if pin_logo.is_touched():
        setVibrationMotor(ON)
        sleep(200)
        setVibrationMotor(OFF)


