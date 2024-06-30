#from math import trunc
import gpiozero
import time
import helpers

#Pin Initalisierung
#Motor A
motorForwardLeftPin = 17
motorReverseLeftPin = 27
motorSpeedLeftPin = 22
#Motor B
motorForwardRightPin = 5
motorReverseRightPin = 6
motorSpeedRightPin = 13
#MotorInitalisierung
forwardLeft = gpiozero.DigitalOutputDevice(motorForwardLeftPin, active_high=True, initial_value=False)
reverseLeft = gpiozero.DigitalOutputDevice(motorReverseLeftPin, active_high=True, initial_value=False)
speedLeft = gpiozero.DigitalOutputDevice(motorSpeedLeftPin, active_high=True, initial_value=1, frequency=100)

forwardRight = gpiozero.DigitalOutputDevice(motorForwardRightPin, active_high=True, initial_value=False)
reverseRight = gpiozero.DigitalOutputDevice(motorReverseRightPin, active_high=True, initial_value=False)
speedRight = gpiozero.PWMOutputDevice(motorSpeedRightPin, active_high=True, initial_value=1, frequency=100)
#Liniensensor
lineSensorLeftPin = gpiozero.LineSensor()
lineSensorMidPin = gpiozero.LineSensor()
lineSensorRightPin = gpiozero.LineSensor()
#Ultraschallsensor
ultraschallSensor = gpiozero.DistanceSensor(echo=23, trigger=24)
ultraschallServo = gpiozero.Servo(21)



#falls def drive nt funktionieren sollte>
"""def forward():
  forwardLeft.on()
  forwardRight.on()

def right():
  forwardLeft.on()
  reverseRight.on()

def left():
  reverseLeft.on()
  forwardRight.on()

def stop():
  forwardLeft.off()
  forwardRight.off()
  reverseLeft.off()
  reverseRight.off()"""

def drive(speed = 1.0, steer = 0.0):
  right = 0.0
  left = 0.0
  if (speed == 0 and not steer == 0):
    left = 1*steer
    right = -1*steer
  elif (speed == 0 and steer == 0)
    
    if steer < 0:
      left = helpers.map(steer, -1, 0, 0, speed)
      right = speed
    elif steer > 0:
      right = helpers.map(steer, -1, 0, 0, speed)
      left = speed
    elif steer == 0:
      left,right = speed,speed
    
    if left > 0:
      forwardLeft.on()
      reverseLeft.off()
    elif left < 0:
      reverseLeft.on()
      forwardLeft.off()
    if right > 0:
      forwardRight.on()
      reverseRight.off()
    elif right < 0:
      reverseRight.on()
      forwardRight.off()
    left = abs(left)
    right = abs(right)
    speedLeft.value = left
    speedRight.value = right

while True:
  #Liniensensor funktion
  if lineSensorMidPin:
    drive()
  elif lineSensorRightPin: 
    drive(0,1)
  elif lineSensorLeftPin:
    drive(0, -1)

#Ultraschallsensor funktion
while True:
  if ultraschallSensor.distance*100 < 5:
    left()
  elif:
    forward()
  if ultraschallServo.value == 1:
    
    
  


  

  """speedLeft.value = 1.0
  speedRight.value = 1.0
  forwardDrive()
  print("drive")
  print(forwardLeft.value)
  print(forwardRight.value)
  print(reverseLeft.value)
  print(reverseRight.value)
  time.sleep(5)
  stop()
  print("stop")
  print(forwardLeft.value)
  print(forwardRight.value)
  print(reverseLeft.value)
  print(reverseRight.value)
  time.sleep(5)"""
  