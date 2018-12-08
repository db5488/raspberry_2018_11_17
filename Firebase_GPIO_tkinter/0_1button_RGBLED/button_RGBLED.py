from gpiozero import RGBLED
from time import sleep

led = RGBLED(red=17, green=27, blue=22);
led.blue = 1;
sleep(1);

led.color = (1, 0, 0); #full green
sleep(1);
led.color = (1, 0, 1); # magenta
sleep(1);
led.color = (1, 1, 0); # yellow
sleep(1);
led.color = (0, 1, 1); #cyan
sleep(1);
led.color = (1, 1, 1); #white
sleep(1);
led.color = (0, 0, 0);
sleep(1);

for n in range(100):
    led.blue = n/100;
    sleep(0.1);
