import RPi.GPIO as GPIO
import time

pins = (4,17,27,22,23,24,25,18);
digits = {
    '.':(0,0,0,0,0,0,0,1),
    '0':(1,1,1,0,1,1,1,0),
    '1':
    }
GPIO.setwarnings(False);
GPIO.setmode(GPIO.BCM);
GPIO.setup(17,GPIO.OUT);
GPIO.output(17, GPIO.HIGH);
time.sleep(10);
GPIO.cleanup();
