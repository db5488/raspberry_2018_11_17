from tkinter import *

def appInterface(window):
    print(window);


if __name__ == '__main__':
    app = Tk();
    app.title("LEDControl");
    app.geometry("500x500");
    app.option_add("*Button.Background","#007A9B");
    app.option_add("*Button.Foreground","#white");
    appInterface(window=app);
    app.mainloop();

