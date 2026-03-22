from microbit import *

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
        pulse_width = max(self.min_pulse, min(self.max_pulse, pulse_width))
        analog_value = int((pulse_width / self.period) * 1023)
        self.pin.write_analog(analog_value)

def battery_level():
    """
    Read battery level from analog pin P2
    Assumes voltage divider (6:1) for measuring 0-6V battery
    Returns battery percentage (0-100)
    """
    # Read analog value from pin2 (0-1023)
    bat_level = pin2.read_analog()
    
    # Map the analog reading to voltage (0-1023 corresponds to 0-3.3V)
    # With 6:1 voltage divider: 6V battery -> 1V at ADC input
    # ADC reference: 3.3V, 10-bit (0-1023)
    
    # Calculate voltage at ADC pin
    adc_voltage = bat_level * 3.3 / 1023
    
    # Calculate actual battery voltage (with 6:1 divider)
    battery_voltage = adc_voltage * 6
    
    # Define voltage range for 0-100% (adjust based on your battery)
    # Typical: 4.5V (0%) to 6.0V (100%) for 6V battery
    min_voltage = 4.5  # 0% charge
    max_voltage = 6.0  # 100% charge
    
    # Convert to percentage
    if battery_voltage >= max_voltage:
        percentage = 100
    elif battery_voltage <= min_voltage:
        percentage = 0
    else:
        percentage = (battery_voltage - min_voltage) / (max_voltage - min_voltage) * 100
    
    return round(percentage)
    
# Show happy face
display.show(Image.HAPPY)
sleep(100)

# Create servo object
servo1 = Servo(pin13)
servo2 = Servo(pin14)
servo3 = Servo(pin15)
servo4 = Servo(pin16)

# Initialize the servo to 0 degrees
servo1.set_angle(0)
servo2.set_angle(0)
servo3.set_angle(0)
servo4.set_angle(0)

# The four servos slowly turn from 0 degrees to 90 degrees
for i in range(90):  
    servo1.set_angle(i)
    servo2.set_angle(i)
    servo3.set_angle(i)
    servo4.set_angle(i)
    sleep(20)

# Cycle read battery voltage
while True:   
    display.scroll(battery_level())
    sleep(2000)
    

