
import RPi.GPIO as GPIO
import time
import picamera
import os
from datetime import datetime

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.IN)         #Read output from PIR motion sensor

camera = picamera.PiCamera()
camera.resolution = tuple([640, 480])
camera.framerate = 16
camera.brightness = 60

while True:
       i=GPIO.input(4)
       print i
       if i==0:                 #When output from motion sensor is LOW
             print "No intruders",i
             time.sleep(0.1)
       else:               #When output from motion sensor is HIGH
             print "Intruder detected",i
             t = datetime.now()
             filename = "capture-%04d%02d%02d-%02d%02d%02d.h264" % (t.year, t.month, t.day, t.hour, t.minute, t.second)
             #camera.capture("raspistill -w 1296 -h 972 -t 0 -e png -q 15 -o %s" % filename)
             print("Captured %s" % filename)
             camera.start_recording(filename)
             time.sleep(10)
             camera.stop_recording()
             time.sleep(0.1)
             
