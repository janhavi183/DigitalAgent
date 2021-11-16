from tkinter import *
from newbackend import  Database
from tkinter import messagebox
from tkinter.ttk import Treeview

database = Database("Property.db")

class RegisterWindow(object):
    def __init__(self,window):
        self.window = window
        self.window.wm_title("Register")
        window.geometry("750x500")

        l1 = Label(window, text="Name",font=('arial',10,'bold'),bd=2)
        l1.grid(row=1, column=0,pady=5)

        l2 = Label(window, text="Contact number",font=('arial',10,'bold'),bd=2)
        l2.grid(row=3, column=0,pady=5)

        l3 = Label(window, text="Email",font=('arial',10,'bold'),bd=2)
        l3.grid(row=5, column=0,pady=5)

        l4 = Label(window, text="Password",font=('arial',10,'bold'),bd=2)
        l4.grid(row=6, column=0,pady=5)

        l5 = Label(window, text="RoleId",font=('arial',10,'bold'),bd=2)
        l5.grid(row=7, column=0,pady=5)

        l6 = Label(window, text="Pincode",font=('arial',10,'bold'),bd=2)
        l6.grid(row=9, column=0,pady=5)


        self.Name_text = StringVar()
        self.e1 = Entry(window, textvariable=self.Name_text)
        self.e1.grid(row=1, column=1,pady=5)

        self.Contact_text = StringVar()
        self.e2 = Entry(window, textvariable=self.Contact_text)
        self.e2.grid(row=3, column=1,pady=5)

        self.Email_text = StringVar()
        self.e3 = Entry(window, textvariable=self.Email_text)
        self.e3.grid(row=5, column=1,pady=5)

        self.Password_text = StringVar()
        self.e4= Entry(window, textvariable=self.Password_text)
        self.e4.grid(row=6, column=1,pady=5)

        self.RoleId_text = StringVar()
        self.e5= Entry(window, textvariable=self.RoleId_text)
        self.e5.grid(row=7, column=1,pady=5)

        self.Pincode_text = StringVar()
        self.e6= Entry(window, textvariable=self.Pincode_text)
        self.e6.grid(row=9, column=1,pady=5)



        b1 = Button(window, text="Register",font=('arial',10,'bold'),bd=2, width=12, command=self.add1_command)
        b1.grid(row=10, column=1,pady=5)
        b2 = Button(window, text="Close",font=('arial',10,'bold'),bd=2, width=12, command=window.destroy)
        b2.grid(row=10, column=2,pady=5)

    def add1_command(self):
         database.insertUser(self.Name_text.get(),self.Contact_text.get(),self.Email_text.get(),self.Password_text.get(),self.RoleId_text.get(),self.Pincode_text.get())
         messagebox.showinfo("Message","User Added Successfully")
         #self.delete(0, END)
         #self.insertUser(END,(self.Name_text.get(),self.Contact_text.get(),self.Email_text.get(),self.Password_text.get(),self.RoleId_text.get(),self.Pincode_text.get()))
        

    

#code for the GUI (front end)
#window = Tk()
#Window(window)

#window.mainloop()
