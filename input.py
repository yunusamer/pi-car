#this will handle the input
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

a_pin = 18
b_pin = 24

# create discharge function for reading capacitor data
def discharge():
    GPIO.setup(a_pin, GPIO.IN)
    GPIO.setup(b_pin, GPIO.OUT)
    GPIO.output(b_pin, False)
    time.sleep(0.005)

# create time function for capturing analog count value
def charge_time():
    GPIO.setup(b_pin, GPIO.IN)
    GPIO.setup(a_pin, GPIO.OUT)
    count = 0
    GPIO.output(a_pin, True)
    while not GPIO.input(b_pin):
	count = count +1
    return count

# create analog read function for reading charging and discharging data
def analog_read():
    discharge()
    return charge_time()

# provide a loop to display analog data count value on the screen
try:
    while True:
        print(analog_read())
        time.sleep(1)

except KeyboardInterrupt:
    print("\n")

finally:
    GPIO.cleanup()
