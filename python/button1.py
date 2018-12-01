from gpiozero import Button, LED
from signal import pause

def userPressed():
    led.toggle();
    print("pressed");

def userReleased():
    #led.off();
    print("released");

led = LED(27)
button = Button(17);
button.when_pressed = userPressed;
button.when_released = userReleased;

pause();
