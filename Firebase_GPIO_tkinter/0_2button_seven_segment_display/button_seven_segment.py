import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False);
GPIO.setmode(GPIO.BCM);
GPIO.setup(17,GPIO.OUT);
GPIO.output(17, GPIO.HIGH);
