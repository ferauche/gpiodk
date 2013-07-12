#!/usr/python

from time import sleep
import RPi.GPIO as GPIO

def init_env():
	GPIO.setmode(GPIO.BOARD)
	GPIO.setwarnings(False)

def init_pin():
	GPIO.setup(10,GPIO.OUT)
	GPIO.setup(11,GPIO.OUT)
	GPIO.setup(12,GPIO.OUT)
	GPIO.setup(13,GPIO.OUT)
	GPIO.setup(21,GPIO.OUT)
	GPIO.setup(22,GPIO.OUT)
	GPIO.setup(23,GPIO.OUT)
	GPIO.setup(24,GPIO.OUT)
	all_low()

def all_low():
	GPIO.output(10,0)
	GPIO.output(11,0)
	GPIO.output(12,0)
	GPIO.output(13,0)
	GPIO.output(21,0)
	GPIO.output(22,0)
	GPIO.output(23,0)
	GPIO.output(24,0)

def all_high():
	GPIO.output(10,1)
	GPIO.output(11,1)
	GPIO.output(12,1)
	GPIO.output(13,1)
	GPIO.output(21,1)
	GPIO.output(22,1)
	GPIO.output(23,1)
	GPIO.output(24,1)

def super_maquina():
	output = 1
	while(output>=0):
		for p in range(10,14):
			GPIO.output(p,output)
			sleep(0.25)
		for p in range(21,25):
			GPIO.output(p,output)
			sleep(0.25)
		output=output-1
	output=1
	while(output>=0):
		for p in range(24,20,-1):
			GPIO.output(p,output)
			sleep(0.25)
		for p in range(13,9,-1):
			GPIO.output(p,output)
			sleep(0.25)
		output=output-1


###################
# Inicio programa #
###################

init_env()
init_pin()

for i in range(0,5):
	all_high()
	sleep(0.5)
	all_low()
	sleep(0.5)

super_maquina()

all_low()
