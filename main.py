#from math import trunc
import gpiozero
import time

#Motor A
motorForwardLeftPin = 17
motorReverseLeftPin = 27
motorSpeedLeftPin = 22
  
#Motor B
motorForwardRightPin = 5
motorReverseRightPin = 6
motorSpeedRightPin = 13

#Liniensensor
#lineSensorLeftPin = gpiozero.LineSensor()
#lineSensorMidPin = gpiozero.LineSensor()
#lineSensorRightPin = gpiozero.LineSensor()
print(motorForwardLeftPin)

forwardLeft = gpiozero.DigitalOutputDevice(motorForwardLeftPin)
reverseLeft = gpiozero.DigitalOutputDevice(motorReverseLeftPin)
speedLeft = gpiozero.PWMOutputDevice(motorSpeedLeftPin)
forwardRight = gpiozero.DigitalOutputDevice(motorForwardRightPin)
reverseRight = gpiozero.DigitalOutputDevice(motorReverseRightPin)
speedRight = gpiozero.PWMOutputDevice(motorSpeedRightPin)



def stop():
  forwardLeft.off()
  forwardRight.off()
  reverseLeft.off()
  reverseRight.off()

def forwardDrive():
  forwardLeft.on()
  reverseLeft.off()
  forwardRight.on()
  reverseRight.off()

def reverseDrive():
  forwardLeft.value = 0
  reverseLeft.value = 1.0
  forwardRight.value = 0
  reverseRight.value = 1.0

def rightTurn():
  forwardLeft.value = 1.0
  reverseLeft.value = 0
  forwardRight.value = 0
  reverseRight.value = 1.0

def leftTurn():
  forwardLeft.value = False
  reverseLeft.value = True
  forwardRight.value = True
  reverseRight.value = False

while True:
  speedLeft.value(1.0)
  speedRight.value(1.0)
  forwardDrive()
  time.sleep(5)
  stop()
  time.sleep(5)
  