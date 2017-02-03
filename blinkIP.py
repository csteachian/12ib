# Blinking IP octet utility
# By Ian Simpson @familysimpson

import socket
import RPi.GPIO as GPIO
import time

def init():
  GPIO.setmode(GPIO.BCM)
  GPIO.setwarnings(False)
  GPIO.setup(21, GPIO.OUT)
  GPIO.output(21, GPIO.LOW)

def get_local_ip_address(target):
  ipaddr = ''
  try:
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect((target, 8000))
    ipaddr = s.getsockname()[0]
    s.close()
  except:
    ipaddr = '0.0.0.0'
    pass

  return ipaddr

def make_binary(value):
  binary = ''
  divisor = 7
  while divisor > -1:
    if value // 2**divisor == 0:
      binary = binary + '0'
    else:
      binary = binary + '1'
      value = value - 2**divisor
    divisor = divisor - 1
  return binary

def blink(value):
  if value == 0:
    timer = 0.1
  else:
    timer = 1
  GPIO.output(21, GPIO.HIGH)
  time.sleep(timer)
  GPIO.output(21, GPIO.LOW)
  time.sleep(0.8)



init()
print("Raspberry Pi - Local IP Address")
ip = (get_local_ip_address('10.0.1.1'))
print(ip)

device = int(ip[ip.rfind('.')+1:])
binary = make_binary(device)

count = 0
time.sleep(3)
while count < 3:
  for index in range(0,len(binary)):
    blink(int(binary[index:index+1]))
  count += 1
  time.sleep(2)