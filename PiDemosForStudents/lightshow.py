import time
import random
import RPi.GPIO as GPIO

#make lights attached to raspberry pi blink!

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(18,GPIO.OUT)
GPIO.setup(23,GPIO.OUT)
GPIO.setup(24,GPIO.OUT)
GPIO.setup(25,GPIO.OUT)

for x in range (0,60):
    for y in range (1,5):
        z = random.randint(1,5)
        a = 0
        if z == 1:
            a=18
        elif z == 2:
            a=23
        elif z == 3:
            a=24
        else:
            a=25
        GPIO.output(a,GPIO.HIGH)
        time.sleep(.25)
        GPIO.output(a,GPIO.LOW)
        #print "im doin it"


print "shows over"
