from gpiozero import Button, LED


button = Button(17)
led = LED(27);
while True:
    if button.is_pressed :
        print('按下');
        led.on();
    else:
        print('放開');
        led.off();


