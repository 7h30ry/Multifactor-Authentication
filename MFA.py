from twilio.rest import Client
import random
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk

class otp_verifier(Tk):
    def __init__(self):
        super().__init__()
        self.geometry("600x550")
        self.resizable(False, False)
        self.n = random.randint(1000,9999)
        self.client=Client("AC2c8ba9b204452737dd2be7298c7ea30a","11f9b2e9304965dab71ce951388f981c") #Put your Account_sid and AUTH Token you got from twilio
        self.client.messages.create(to="+2349018955027", #Phone number you are sendig otp to 
                                    from_="+13393453079",# Phone number for dending otp given to you by twilio
                                    body=self.n)
 
    def Labels(self):
        self.c = Canvas(self,bg="white",width=400,height=280)
        self.c.place(x=100,y=90)

        self.Login_Title=Label(self,text="OTP Verification",font="bold, 20",bg="white")
        self.Login_Title.place(x=210,y=90)
    
    def Entry(self):
        self.User_Name=Text(self, borderwidth=2, wrap="word", width=29, height=2)
        self.User_Name.place(x=190,y=160)

    def Buttons(self):
        #self.submitButtonImage=PhotoImage(file="submit.png")
        #self.submitButtonImage=Button(self, '''image=self.submitButtonImage''',text="SUBMIT",command=self.checkOTP,border=0,bg="red")
        self.submitbtn=Button(self, text = 'SUBMIT', bd = '5',command=self.checkOTP)
        self.submitbtn.place(x=195,y=210)

        #self.resendOTPImage=PhotoImage(file="thenounproject.png")
        #self.resendOTPImage=Button(self, '''image=self.resendOTPImage''',text="RESEND OTP",command=self.resendOTP,border=0, bg="blue")
        self.resendOTPbtn=Button(self, text = 'RESEND OTP', bd = '5',command=self.resendOTP)
        self.resendOTPbtn.place(x=208,y=400)

    def checkOTP(self):
        try:
            self.userInput=int(self.User_Name.get(1.0, "end-1c"))
            if self.userInput==self.n:
                messagebox.showinfo("showinfo", "Login Success")
                self.n="done"

            elif self.n=="done":
                messagebox.showinfo("showinfo","Already Entered the OTP")
            else:
                messagebox.showinfo("showinfo", "Wrong OTP")
        except:
            messagebox.showinfo("showinfo", "INVALID OTP")

            

    def resendOTP(self):
        self.n = random.randint(1000,9999)
        self.client=Client("AC2c8ba9b204452737dd2be7298c7ea30a","11f9b2e9304965dab71ce951388f981c")
        self.client.messages.create(to="+2349018955027",
                                    from_="+13393453079",
                                    body=self.n)

if __name__=="__main__":
    window=otp_verifier()
    window.Labels()
    window.Entry()
    window.Buttons()
    window.mainloop()