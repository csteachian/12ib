#!/usr/bin/env python
#Simply tries to swithc Pin 11 on for 1 sec and off for 2 secs
#V0.2 26Aug12

# Must be run as root - sudo python blink11.py 

import time, RPi.GPIO as Ian

Ian.setmode(Ian.BOARD)
Ian.setup(11, Ian.OUT)
Ian.setup(13, Ian.OUT)
Ian.setup(15, Ian.IN)

while True:
	if(Ian.input(15)==0):
		LEDon = Ian.output(11, 1)
		time.sleep(1)
		LEDoff = Ian.output(11, 0)
		time.sleep(0.5)
		BUZZon = Ian.output(13, 1)
		time.sleep(0.5)
		BUZZoff = Ian.output(13, 0)
		time.sleep(1)

