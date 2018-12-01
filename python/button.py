from gpiozero import Button

button = Button(17)
while True:
    print(button.is_pressed);

