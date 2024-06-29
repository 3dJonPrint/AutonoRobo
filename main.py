import gpiozero
import time

#Motor A
motorForwardLeftPin = 26
motorReverseLeftPin = 19
motorSpeedLeftPin = 
  
#Motor B
motorForwardRightPin = 13
motorReverseRightPin = 6
motorSpeedRightPin = 

forwardLeft = gpiozero.PWMOutputDevice(motorForwardLeftPin, True, 0, 1000)
reverseLeft = gpiozero.PWMOutputDevice(motorReverseLeftPin, True, 0, 1000)
speedLeft = gpiozero.PWMOutputDevice(motorSpeedLeftPin, True, 0, 1000)

forwardRight = gpiozero.PWMOutputDevice(motorForwardRightPin, True, 0, 1000)
reverseRight = gpiozero.PWMOutputDevice(motorReverseRightPin, True, 0, 1000)
speedRight = gpiozero.PWMOutputDevice(motorSpeedRightPin, True, 0, 1000)

def stop():
  forwardLeft.value = 0
  forwardRight.value = 0
  reverseLeft.value = 0
  reverseRight.value = 0

def forwardDrive():
  forwardLeft.value = 1.0
  reverseLeft.value = 0
  forwardRight.value = 1.0
  reverseRight.value = 0

def main():
  forwardDrive()
  time.sleep(5)
  stop()
  time.sleep(5)