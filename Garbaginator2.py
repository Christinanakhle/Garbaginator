GPIO.setup(17,GPIO.OUT)

def RCtime (PiPin):
    measurement = 0
    GPIO.setup(PiPin,GPIO.OUT)
    GPIO.output(PiPin,GPIO.LOW)
    time.sleep(0.1)

    GPIO.setup(PiPin,GPIO.IN)

    while (GPIO.input(PiPin)== GPIO.LOW):

        measurement +=1

    if ( measurement > 100):
        print ("TEST")

        tau = (measurement/(28.6*(10**4)))
        res = (tau*(10**6))-(10**4)

        if (res>10):
            print ("RESISTANCE")
            print ("MOTOR ON")
            GPIO.OUTPUT(17,GPIO.HIGH)
            time.sleep(2)
            GPIO.output(17,GPIO.LOW)
            time.sleep(2)



        return measurement

while True:
    print (RCtime(4))
