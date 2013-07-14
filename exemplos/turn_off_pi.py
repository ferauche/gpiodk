#!/usr/python

from os import system
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

def callback_off(channel):
	print("Botão pressionado no pino ",channel)
	print("Desligando o Raspberry PI")
	system("shutdown -h now")

def callback_exit(channel):
	print("Botão pressionado no pino ",channel)
	print("Saindo do programa.")
	quit()

###################
# Inicio programa #
###################

init_env()
init_pin()

GPIO.add_event_detect(19, GPIO.FALLING, callback_off)
GPIO.add_event_detect(18, GPIO.FALLING, callback_exit)

print("Pressione os botões dos pinos abaixo para: ")
print("Botão pino 18...: Sair do programa")
print("Botão pino 19...: Desligar o Raspberry PI")

loop=True
while(loop):
	loop=True
