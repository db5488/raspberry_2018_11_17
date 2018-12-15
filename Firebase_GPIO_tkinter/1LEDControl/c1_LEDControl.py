from tkinter import *

def ledClose():
    print("ledClose");
    
def ledOpen():
    print("ledOpen");

def appInterface(window):
    frame = Frame(window,borderwidth=1,relief=GROOVE);
    Label(frame,
          text="LED Controler",
          font=("Helvetica", 20)
          ,anchor=W).pack(fill=X);
    
    Button(frame,text="open",
           pady=50,
           font=("Helvetica", 20),
           command=ledOpen).pack(side=LEFT,
                                        fill=X,
                                        expand=True,
                                        padx=10,
                                        pady=20);
    
    Button(frame,text="close"
           ,pady=50,           
           font=("Helvetica", 20),command=ledClose).pack(side=LEFT,
                                        fill=X,
                                        expand=True,
                                        padx=10,
                                        pady=20);
    frame.pack(padx=10,pady=10,fill=X);


if __name__ == '__main__':
    app = Tk();
    app.title("LEDControl");
    app.geometry("500x500");
    app.option_add("*Button.Background","#007A9B");
    app.option_add("*Button.Foreground","white");
    appInterface(window=app);
    app.mainloop();

