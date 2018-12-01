from gpiozero import Button

button = Button(17)
while True:
    if button.is_pressed :
        print('按下');
    else:
        print('放開');


