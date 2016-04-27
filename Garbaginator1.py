import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)

PIR_PIN = 4
GPIO.setup(PIR_PIN, GPIO.IN)
GPIO.setup(18,GPIO.OUT)
try:
    print("PIR Module test (CTRL+c to exit)")
    time.sleep(2)
    print("ready")

    while True:

        if GPIO.input(PIR_PIN):
            print("Motion detected")
            print("Laser ON")
            GPIO.output(18,GPIO.HIGH)
            time.sleep(1)
            GPIO.output(18,GPIO.LOW)
            time.sleep(1)

        else:
            print("no motion")
            time.sleep(2)


except KeyboardInterrupt:
    print("Quit")
    GPIO.cleanup()
