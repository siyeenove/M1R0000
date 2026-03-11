# Imports go at the top
from microbit import *

# Servo class
class Servo:
    # The constructor of a class
    def __init__(self, pin):
        self.pin = pin
        # Servo parameters
        self.min_pulse = 500    # Pulse width at 0 degrees (microseconds)
        self.max_pulse = 2400   # Pulse width at 180 degrees (microseconds)
        self.period = 20000     # 20ms period (50Hz)
        self.pin.set_analog_period(20)  # Set period to 20ms

    # Set the servo Angle function
    def set_angle(self, angle):
        # Limit angle range
        angle = max(0, min(180, angle))
        
        # Calculate pulse width
        pulse_width = self.min_pulse + (angle / 180) * (self.max_pulse - self.min_pulse)
        
        # Convert to analog value (0-1023)
        analog_value = int((pulse_width / self.period) * 1023)
        
        # Set PWM
        self.pin.write_analog(analog_value)

    # Set the servo Angle function using pulse width
    def set_pulse(self, pulse_width):
        # Limit the maximum pulse value
        pulse_width = max(self.min_pulse, min(self.max_pulse, pulse_width))
        
        # Calculate pulse
        analog_value = int((pulse_width / self.period) * 1023)
        
         # Set PWM
        self.pin.write_analog(analog_value)
    
# Show happy face
display.show(Image.HAPPY)
# delay 100 milliseconds
sleep(100)  

# Create 4 servo objects and define the pins to use
servo1 = Servo(pin13)  # servo1 uses pin13
servo2 = Servo(pin14)  # servo2 uses pin14
servo3 = Servo(pin15)  # servo3 uses pin15
servo4 = Servo(pin16)  # servo4 uses pin16

# Initialize the angles of the 4 servos
servo1.set_angle(90)  # Set the Angle of servo1
sleep(500)            # delay 500 milliseconds
servo2.set_angle(90)  # Set the Angle of servo2
sleep(500)            # delay 500 milliseconds
servo3.set_angle(60)  # Set the Angle of servo3
sleep(500)            # delay 500 milliseconds
servo4.set_angle(90)  # Set the Angle of servo4
sleep(500)            # delay 500 milliseconds

# Let servo 3 swing between 0 and 60 degrees.
while True:   
    # The servo swings from 60 degrees to 0 degrees
    for i in range(60):  
        # Set the Angle of servo3
        servo3.set_angle(60-i)
        # delay 20 milliseconds
        sleep(20)

    # The servo swings from 0 degrees to 60 degrees
    for i in range(60):  
        # Set the Angle of servo3
        servo3.set_angle(i)
        # delay 20 milliseconds
        sleep(20)
    

