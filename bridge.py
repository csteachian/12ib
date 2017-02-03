import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

pinMotorAForwards = 10
pinMotorABackwards = 9
pinMotorBForwards = 8
pinMotorBBackwards = 7

GPIO.setup(pinMotorAForwards, GPIO.OUT)
GPIO.setup(pinMotorABackwards, GPIO.OUT)
GPIO.setup(pinMotorBForwards, GPIO.OUT)
GPIO.setup(pinMotorBBackwards, GPIO.OUT)

def StopMotors():
	GPIO.output(pinMotorAForwards, 0)
	GPIO.output(pinMotorABackwards, 0)
	GPIO.output(pinMotorBForwards, 0)
	GPIO.output(pinMotorBBackwards, 0)

def Forwards():
	GPIO.output(pinMotorAForwards, 1)
	GPIO.output(pinMotorABackwards, 0)
	GPIO.output(pinMotorBForwards, 1)
	GPIO.output(pinMotorBBackwards, 0)

def Backwards():
	GPIO.output(pinMotorAForwards, 0)
	GPIO.output(pinMotorABackwards, 1)
	GPIO.output(pinMotorBForwards, 0)
	GPIO.output(pinMotorBBackwards, 1)

def Left():
	GPIO.output(pinMotorAForwards, 0)
	GPIO.output(pinMotorABackwards, 1)
	GPIO.output(pinMotorBForwards, 1)
	GPIO.output(pinMotorBBackwards, 0)

def Right():
	GPIO.output(pinMotorAForwards, 1)
	GPIO.output(pinMotorABackwards, 0)
	GPIO.output(pinMotorBForwards, 0)
	GPIO.output(pinMotorBBackwards, 1)

print("bridge test")
Forwards()
time.sleep(1.5)
StopMotors()
#time.sleep(1)
#Left()
#time.sleep(0.3)
#Right()
#time.sleep(0)
#Backwards()
#time.sleep(0)
#StopMotors()
GPIO.cleanup()
