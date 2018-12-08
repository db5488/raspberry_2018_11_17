from gpiozero import RGBLED
from time import sleep

led = RGBLED(red=17, green=27, blue=22);
led.blue = 1;
sleep(1);