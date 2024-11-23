"""
This Raspberry Pi code was developed by newbiely.com
This Raspberry Pi code is made available for public use without any restriction
For comprehensive instructions and wiring diagrams, please visit:
https://newbiely.com/tutorials/raspberry-pi/raspberry-pi-keypad
"""


import RPi.GPIO as GPIO
import time

# Define keypad layout
KEYPAD = [
    [1, 2, 3, 'A'],
    [4, 5, 6, 'B'],
    [7, 8, 9, 'C'],
    ['*', 0, '#', 'D']
]

# Define GPIO pins for rows and columns
ROWS = [4, 17, 27, 22]
COLS = [5, 6, 13, 19]

# Initialize GPIO
GPIO.setmode(GPIO.BCM)

# Set up row pins as inputs with pull-up resistors
for row_pin in ROWS:
    GPIO.setup(row_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# Set up column pins as outputs
for col_pin in COLS:
    GPIO.setup(col_pin, GPIO.OUT)
    GPIO.output(col_pin, GPIO.HIGH)

def get_key():
    key = None

    # Scan each column
    for col_num, col_pin in enumerate(COLS):
        GPIO.output(col_pin, GPIO.LOW)

        # Check each row
        for row_num, row_pin in enumerate(ROWS):
            if GPIO.input(row_pin) == GPIO.LOW:
                key = KEYPAD[row_num][col_num]

                # Wait for key release
                while GPIO.input(row_pin) == GPIO.LOW:
                    time.sleep(0.05)

        GPIO.output(col_pin, GPIO.HIGH)

    return key

try:
    while True:
        print("Reading...")
        pressed_key = get_key()

        if pressed_key is not None:
            print(f"Pressed: {pressed_key}")
        time.sleep(0.1)

except KeyboardInterrupt:
    GPIO.cleanup()
