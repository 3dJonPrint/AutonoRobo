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
speedLeft = gpiozero.PWMOutputDevice(motorSpeedLeftPin, active_high=True, initial_value=1, frequency=100)

forwardRight = gpiozero.DigitalOutputDevice(motorForwardRightPin, active_high=True, initial_value=False)
reverseRight = gpiozero.DigitalOutputDevice(motorReverseRightPin, active_high=True, initial_value=False)
speedRight = gpiozero.PWMOutputDevice(motorSpeedRightPin, active_high=True, initial_value=1, frequency=100)

#Liniensensor
lineSensorLeftPin = gpiozero.LineSensor(23)
lineSensorMidPin = gpiozero.LineSensor(24)
lineSensorRightPin = gpiozero.LineSensor(25)

#Ultraschallsensor
ultraschallSensor = gpiozero.DistanceSensor(echo=12, trigger=16, threshold_distance = 0.05)
ultraschallServo = gpiozero.Servo(26)

#Ultraschallsensor funktion
def turnAround():
  ultraschallServo.min()
  distanceLeft = ultraschallSensor.distance*100
  time.sleep(0.5)
  ultraschallServo.max()
  distanceRight = ultraschallSensor.distance*100
  time.sleep(0.5)
  if distanceLeft < distanceRight:
    drive(0,1)
    time.sleep(0.5)
  elif distanceLeft > distanceRight:
    drive(0,-1)
    time.sleep(0.5)
    
#Fahrfunktion
def drive(speed = 1.0, steer = 0.0):
  brake = False
  right = 0.0
  left = 0.0
  if (speed == 0 and not steer == 0):
    left = 1.0*steer
    right = -1.0*steer
  elif (speed == 0 and steer == 0):
    brake = True
    forwardLeft.on()
    forwardRight.on()
    reverseLeft.on()
    reverseRight.on()
    left = 1
    right = 1
  else:
    if steer < 0:
      left = helpers.map(steer, -1, 0, 0, speed)
      right = speed
    elif steer > 0:
      right = helpers.map(steer, 0, 1, speed, 0)
      left = speed
    elif steer == 0:
      left,right = speed,speed
  if not brake:
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
  print(left,right)
  left = abs(left)
  right = abs(right)
  print(left,right)
  speedLeft.value = left
  speedRight.value = right

#Liniensensor funktion
def linesensordrive():
  ll = lineSensorLeftPin.line_detected
  lm = lineSensorMidPin.line_detected
  lr = lineSensorRightPin.line_detected
  #ultraschallSensor.when_in_range(turnAround)
  if (not ll and lm and not lr):
    drive(0.3, 0)
    print("mid")
  elif ( ll and lm and lr):
    drive(0.3, 0)
    print("all")
  elif (not ll and not lm and lr):
    drive(0,0.4)
    print("right")
    time.sleep(0.1)
  elif ( ll and not lm and not lr):
    drive(0, -0.4)
    print("left")
    time.sleep(0.1)
  elif (not ll and not lm and not lr):
    drive(0.3, 0)
    print("nothing")
  elif ( ll and lm and not lr):
    drive(0.35, -1)
    print("left mid")
  elif (not ll and lm and lr):
    drive(0.4, 1)
    print("mid right")
  elif ( ll and not lm and lr):
    drive(0,0)
    print("left right")

while False:
  drive(0.2, 0)
  print("mid")
  time.sleep(5)
  drive(0.2, 0)
  print("all")
  time.sleep(5)
  drive(0,0.2)
  print("right")
  time.sleep(5)
  drive(0, -0.2)
  print("left")
  time.sleep(5)
  drive(0, 0)
  print("nothing")
  time.sleep(5)
  drive(0.25, -0.5)
  print("left mid")
  time.sleep(5)
  drive(0.3, 0.5)
  print("mid right")
  time.sleep(5)
  drive(0,0)
  print("left right")
  time.sleep(5)

while False:
  ll = lineSensorLeftPin.line_detected
  lm = lineSensorMidPin.line_detected
  lr = lineSensorRightPin.line_detected
  if (not ll and lm and not lr):
    print("mid")
  elif ( ll and lm and lr):
    print("all")
  elif (not ll and not lm and lr):
    print("right")
  elif ( ll and not lm and not lr):
    print("left")
  elif (not ll and not lm and not lr):
    print("nothing")
  elif ( ll and lm and not lr):
    print("left mid")
  elif (not ll and lm and lr):
    print("mid right")
  elif ( ll and not lm and lr):
    print("left right")
  time.sleep(0.5)

while True:
  linesensordrive()
  time.sleep(0.2)

"""while True:
  drive(0.5,0.3)
  print("drive")
  time.sleep(10)
  drive(0.5,-0.3)
  print("stop")
  time.sleep(10)"""




  
  

    
    
  


  

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
  