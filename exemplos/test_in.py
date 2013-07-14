#!/usr/python

from time import sleep
import RPi.GPIO as GPIO

def init_env():
	GPIO.setmode(GPIO.BOARD)
	GPIO.setwarnings(False)

def init_pin():
	GPIO.setup(15,GPIO.IN)
	GPIO.setup(16,GPIO.IN)
	GPIO.setup(18,GPIO.IN)
	GPIO.setup(19,GPIO.IN)

def read_pins(isFirst):
	if(isFirst):
		print("15   16   18   19")
	print(GPIO.input(15),"  ",GPIO.input(16),"  ",GPIO.input(18),"  ",GPIO.input(19))



###################
# Inicio programa #
###################

init_env()
init_pin()

read_pins(True)

for i in range(0,5):
	read_pins(False)
	sleep(1)	
