#!/usr/bin/python
import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setup(33,GPIO.OUT)
GPIO.setup(12,GPIO.OUT)
GPIO.setup(11,GPIO.OUT)


def RCtime (RCpin):
    reading = 0
    GPIO.setup(RCpin,GPIO.OUT)
    GPIO.output(RCpin,GPIO.LOW)
    time.sleep(0.1)

    GPIO.setup(RCpin, GPIO.IN)
    while (GPIO.input(RCpin)==GPIO.LOW):
            reading +=1
    if GPIO.input(12):
        

        if (reading<500): #plastic
            print("PLASTIC")
            GPIO.output(33,GPIO.HIGH)
            time.sleep(2)
            GPIO.output(33,GPIO.LOW)
            time.sleep(2)
            GPIO.output(11,GPIO.HIGH)
            time.sleep(2)
            GPIO.output(11,GPIO.LOW)

        else:#non-plastic
            print("non-plastic")
            GPIO.output(11,GPIO.HIGH)
            time.sleep(2)
            GPIO.output(11,GPIO.LOW)
            time.sleep(2)
            GPIO.output(33,GPIO.HIGH)
            time.sleep(2)
            GPIO.output(33,GPIO.LOW)
    else:
        pass


    return reading





while True:
        print (RCtime(40))
            
