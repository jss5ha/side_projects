import RPi.GPimport RPi.GPIO as GPIO
import time
import random

'''
This is a whack a mole style game meant to be played by attaching lights to 
the GPIO pins of a Raspberry Pi
'''

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(18,GPIO.OUT)
GPIO.setup(23,GPIO.OUT)
GPIO.setup(24,GPIO.OUT)
GPIO.setup(25,GPIO.OUT)
#18 is 1, 23 is 2, 24 is 3, 25 is 4
whacks = 0
play = False
Youwon = False
ready = raw_input("Are you ready to play whack a mole? Yes or No: ")
if ready == "Yes":
    print "How fast can you whack 30 moles without goofing?"
    play = True
    start_time = time.time()
    while play:
        x = random.randint(1,5)
        if x == 1:
            GPIO.output(18,GPIO.HIGH)
            y = int(input())
            if y == 1:
                GPIO.output(18,GPIO.LOW)
                whacks+=1
            else:
                play = False
                print "You goofed! You lose!"
        elif x == 2:
            GPIO.output(23,GPIO.HIGH)
            y = int(input())
            if y == 2:
                GPIO.output(23,GPIO.LOW)
                whacks+=1
            else:
                play = False
                print "You goofed! You lose!"
        elif x == 3:
            GPIO.output(24,GPIO.HIGH)
            y = int(input())
            if y == 3:
                GPIO.output(24,GPIO.LOW)
                whacks+=1
            else:
                play = False
                print "You goofed! You lose!"
        else:
            GPIO.output(25,GPIO.HIGH)
            y = int(input())
            if y == 4:
                GPIO.output(25,GPIO.LOW)
                whacks+=1
            else:
                play = False
                print "You goofed! You lose!"
        if whacks== 30:
            play=False
            print "You Win!"
            print time.time()-start_time
            print "That is your time in seconds!"
else:
    print "Ok, Goodbye."


GPIO.output(18,GPIO.LOW)
GPIO.output(23,GPIO.LOW)
GPIO.output(24,GPIO.LOW)
GPIO.output(25,GPIO.LOW)


