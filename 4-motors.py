import RPi.GPIO as GPIO
import time
import tty
import sys
import termios
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

print("hi")
os = termios.tcgetattr(sys.stdin)
tty.setraw(sys.stdin)
x=0
while x != chr(27): #ESC
    x = sys.stdin.read(1)[0]
    print("You pressed", x)
    if x == "w":
        print("UP")
	Forwards()
	time.sleep(0.1)
	StopMotors()
    elif x == "s":
        print("DOWN")
	Backwards()
        time.sleep(0.1)
        StopMotors()
    elif x == "a":
        print("LEFT")
	Left()
        time.sleep(0.1)
        StopMotors()
    elif x == "d":
        print("RIGHT")
	Right()
        time.sleep(0.1)
        StopMotors()
    else:
        print("DUH")
termios.tcsetattr(sys.stdin, termios.TCSADRAIN, os)
GPIO.cleanup()
