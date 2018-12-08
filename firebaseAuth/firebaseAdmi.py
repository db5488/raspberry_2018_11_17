from tkinter import *
from tkinter import messagebox
import Pmw
import firebase_admin
from firebase_admin import credentials, auth

class App:
    def __init__(self, master):
        self.inputID = Pmw.EntryField(master,
                                 entry_width=20,
                                 value='',
                                 label_text='請輸入Email: ',
                                 labelpos=W,
                                 labelmargin=1);
        self.inputID.pack(padx=15, pady=15);
        
        self.inputPWD = Pmw.EntryField(master,
                                  entry_width=20,
                                  value='',
                                  label_text='請輸入密碼:',
                                  labelpos=W,
                                  labelmargin=1);
        self.inputPWD.pack(padx=15, pady=15);
        
        Button(master,
                        text="確定",
                        command = self.helloCallBack).pack(pady=15, expand=1);
    
    def helloCallBack(self):
        #messagebox.showinfo("Hello python", "Hello world");
        inputEmail = self.inputID.getvalue();
        inputPWD = self.inputPWD.getvalue();
        
        print(self.inputID.getvalue());
        print(self.inputPWD.getvalue());
        
        
        #detrieve user data
        user = auth.get_user_by_email(inputEmail);
        print('custom_claims:',user.custom_claims);

if __name__ == '__main__':
    cred = credentials.Certificate('../privateKey/raspberryfirebase-firebase-adminsdk-q4ht6-92b0f0e25f.json');
    default_app = firebase_admin.initialize_app(cred);
    window = Tk();
    window.title('會員登入');
    window.option_add("*Font",('Arial',18));
    #window.configure(background='#6c6024');
    
   
    app = App(window);
    
    
    #button = messagebox.askquestion("Question:","Oh Dear, did somebody\nsay mattress to Mr Lambert?",default=NO);
    #question.result.setentry(button);
    

    window.mainloop();

    
