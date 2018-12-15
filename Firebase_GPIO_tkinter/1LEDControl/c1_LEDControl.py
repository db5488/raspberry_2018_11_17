from tkinter import *

def appInterface(window):
    frame = Frame(window,borderwidth=1,width=250,height=250,relief=GROOVE);
    frame.pack(padx=10,pady=10,fill=X);


if __name__ == '__main__':
    app = Tk();
    app.title("LEDControl");
    app.geometry("500x500");
    app.option_add("*Button.Background","#007A9B");
    app.option_add("*Button.Foreground","#white");
    appInterface(window=app);
    app.mainloop();

