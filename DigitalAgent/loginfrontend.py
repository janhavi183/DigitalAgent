from tkinter import *
from tkinter import messagebox
from loginbackend import  Database
import agentfrontend as AgentScreen
import ownerpagefrontend as OwnerScreen
import userpagefrontend as BuyerScreen
import newuser as RegisterScreen

import Session as objmanageSession

database = Database("Property.db")

class LoginScreen(object):
    def __init__(self,window):
        self.window = window
        self.window.wm_title("Login")

        l11 = Label(window, text="DigitalAgent",font=('arial',30,'bold'),bd=2)
        l11.grid(row=0, column=1,pady=5)
        
        l1 = Label(window, text="Email:",font=('arial',10,'bold'),bd=2)
        l1.grid(row=1, column=0,pady=5)
        self.Emails_text = StringVar()
        self.e1 = Entry(window, textvariable=self.Emails_text)       
        self.e1.grid(row=1, column=1,pady=5)
        
        l2 = Label(window, text="Password:",font=('arial',10,'bold'),bd=2)
        l2.grid(row=2, column=0,pady=5)    
        self.Passwords_text = StringVar()
        self.e2 = Entry(window,show='*',textvariable=self.Passwords_text)
        self.e2.grid(row=2, column=1,pady=5)
        
        b1 = Button(window, text="Login",font=('arial',10,'bold'),bd=2, width=9, command=self.validate_command)
        b1.grid(row=3, column=0,padx=10,pady=5)
        b2 = Button(window, text="New user",font=('arial',10,'bold'),bd=2, width=9, command=self.Register_command)
        b2.grid(row=3, column=1,padx=10,pady=5)
        b3 = Button(window, text="Close",font=('arial',10,'bold'),bd=2, width=9, command=window.destroy)
        b3.grid(row=3, column=2,padx=10,pady=5)
        
    def validate_command(self):
        #messagebox.showinfo("Messgae",self.Emails_text.get())
        data=database.doLogin(self.Emails_text.get(), self.Passwords_text.get()) 
        if(len(data) > 0):
            #messagebox.showinfo("Messgae",data[0][1]  )
            objmanageSession.SetSession(self.Emails_text.get())
            window.destroy()
            main = Tk()
            if(data[0][1] == "Agent"):
                AgentScreen.AgentWindow(main)
            if(data[0][1] == "Owner"):
                OwnerScreen.OwnerWindow(main)
            if(data[0][1] == "Buyer"):
                BuyerScreen.BuyerWindow(main)
        else:
             messagebox.showerror("Error","Wrong Credentials")

    def Register_command(self):
        window.destroy()
        main = Tk()
        RegisterScreen.RegisterWindow(main)
      

#code for the GUI (front end)
window = Tk()
window.geometry("500x200")
LoginScreen(window)
window.mainloop()
