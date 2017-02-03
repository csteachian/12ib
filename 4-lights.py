#Alberto
import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

PinLDR = 27
def ReadLDR():
	LDRCount = 0
	GPIO.setup(PinLDR, GPIO.OUT)
	GPIO.output(PinLDR, GPIO.LOW)
	time.sleep(0.1)
	GPIO.setup(PinLDR, GPIO.IN)
	while (GPIO.input(PinLDR) == GPIO.LOW):
		LDRCount += 1
	return LDRCount

while True:
	print(ReadLDR())
	if (ReadLDR() > 600):
		
	time.sleep(1)

