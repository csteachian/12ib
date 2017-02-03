# Last edited Mr Simpson 13/1/17

# CamJam EduKit 3 - Robotic
import RPi.GPIO as GPIO # Import the GPIO Library
import time # Import the Time library
import tty
import sys
import termios
# Set the GPIO modes
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
# Set variables for the GPIO motor pins
pinMotorAForwards = 10
pinMotorABackwards = 9 
pinMotorBForwards = 8
pinMotorBBackwards = 7
# Set the GPIO Pin mode
GPIO.setup(pinMotorAForwards, GPIO.OUT)
GPIO.setup(pinMotorABackwards, GPIO.OUT)
GPIO.setup(pinMotorBForwards, GPIO.OUT)
GPIO.setup(pinMotorBBackwards, GPIO.OUT)
# Turn all motors off
def StopMotors():
    GPIO.output(pinMotorAForwards, 0)
    GPIO.output(pinMotorABackwards, 0)
    GPIO.output(pinMotorBForwards, 0)
    GPIO.output(pinMotorBBackwards, 0)
# Turn both motors forwards
def Forwards():
    GPIO.output(pinMotorAForwards, 1)
    GPIO.output(pinMotorABackwards, 0)
    GPIO.output(pinMotorBForwards, 1)
    GPIO.output(pinMotorBBackwards, 0)
# Turn both motors backwards
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
# Turn Right
def Right():
    GPIO.output(pinMotorAForwards, 1)
    GPIO.output(pinMotorABackwards, 0)
    GPIO.output(pinMotorBForwards, 0)
    GPIO.output(pinMotorBBackwards, 1)

os = termios.tcgetattr(sys.stdin)
tty.setraw(sys.stdin)
x = 0
while x != chr(27): #ESC
    x = sys.stdin.read(1)[0]
    print("you pressed", x)
    if x == "w":
        print("UP")
	Forwards()
	time.sleep(0.2)
	StopMotors()
    if x == "s":
        print("DOWN")
	Backwards()
	time.sleep(0.2)
	StopMotors()
    if x == "a":
        print("LEFT")
	Left()
	time.sleep(0.2)
	StopMotors()
    if x == "d":
        print("RIGHT")
	Right()
	time.sleep(0.2)
	StopMotors()
termios.tcsetattr(sys.stdin, termios.TCSADRAIN, os)

Forwards()
time.sleep(1.5)
#Backwards()
time.sleep(1)
StopMotors()
Left()
time.sleep(0.5)
Right()
time.sleep(2)
Forwards()
time.sleep(0.5)
GPIO.cleanup()
