from tkinter import *
from userpagebackend import  Database
from tkinter import messagebox
from tkinter.ttk import Treeview
database = Database("Property.db")


class BuyerWindow(object):
    def __init__(self,window):
        self.window = window
        window.geometry("750x500")
        self.window.wm_title("Buyer")

        l1 = Label(window, text="Property type",font=('arial',10,'bold'),bd=2)
        l1.grid(row=0, column=0,pady=5,sticky=W)

        self.Prop_type_text = StringVar()
        self.e1 = Entry(window, textvariable=self.Prop_type_text)
        self.e1.grid(row=0, column=1,pady=5,sticky=W)

        l2 = Label(window, text="Pincode",font=('arial',10,'bold'),bd=2)
        l2.grid(row=0, column=2,pady=5,sticky=W)

        

        self.Pincode_text = StringVar()
        self.e2 = Entry(window, textvariable=self.Pincode_text)
        self.e2.grid(row=0, column=3,pady=5,sticky=W)

        l3 = Label(window, text="min_cost",font=('arial',10,'bold'),bd=2)
        l3.grid(row=1, column=0,pady=5,sticky=W)

        self.min_cost_text = StringVar()
        self.e3 = Entry(window, textvariable=self.min_cost_text)
        self.e3.grid(row=1, column=1,pady=5,sticky=W)

        l4 = Label(window, text="max_cost",font=('arial',10,'bold'),bd=2)
        l4.grid(row=1, column=2,pady=5,sticky=W)

        self.max_cost_text = StringVar()
        self.e4= Entry(window, textvariable=self.max_cost_text)
        self.e4.grid(row=1, column=3,pady=5,sticky=W)

        b2 = Button(window, text="Search ",font=('arial',10,'bold'),bd=2, width=12, command=self.search_command)
        b2.grid(row=1, column=4,pady=5,sticky=W)

        
        l5 = Label(window, text="Address",font=('arial',10,'bold'),bd=2)
        l5.grid(row=2, column=0,pady=4,sticky=W)

        self.address_text = StringVar()
        self.e5 = Entry(window, textvariable=self.address_text)
        self.e5.grid(row=2, column=1,pady=5,sticky=W)

        l6 = Label(window, text="Cost",font=('arial',10,'bold'),bd=2)
        l6.grid(row=2, column=2,pady=5,sticky=W)

        self.cost_text = StringVar()
        self.e6 = Entry(window, textvariable=self.cost_text)
        self.e6.grid(row=2, column=3,pady=5,sticky=W)




        l7 = Label(window, text="Agent Emailid:",font=('arial',10,'bold'),bd=2)
        l7.grid(row=19, column=0,pady=5,sticky=W)

        self.EmailAgent_text = StringVar()
        self.e7 = Entry(window, textvariable=self.EmailAgent_text)
        self.e7.grid(row=19, column=1,pady=5,sticky=W)


        l10 = Label(window, text="Properties:",font=('arial',10,'bold'),bd=2)
        l10.grid(row=2, column=0 ,pady=5,sticky=W)
        
        self.list2 = Listbox(window, height=3, width=70)
        self.list2.grid(row=2, column=1 ,pady=5,columnspan=3,sticky=W)

        self.list2.bind('<<ListboxSelect>>', self.get_selected_row1)


        sb2 = Scrollbar(window)
        sb2.grid(row=2, column=4,pady=5,sticky=W)
        self.list2.config(yscrollcommand=sb2.set)
        sb2.config(command=self.list2.yview)


        b4=Button(window, text="Inquire",font=('arial',10,'bold'),bd=2, width=12, command=self.add_command)
        b4.grid(row=20, column=1)
        b6 = Button(window, text="Close",font=('arial',10,'bold'),bd=2, width=12, command=window.destroy)
        b6.grid(row=20, column=2)
        
            
    def add_command(self):
        database.insertrequirement(self.Prop_type_text.get(), self.Pincode_text.get(),self.address_text.get(),self.cost_text.get(),self.EmailAgent_text.get())
        messagebox.showinfo("Message","Property Inquiry Added Successfully") 

    def search_command(self):
        self.list2.delete(0, END)
        pincode = self.Pincode_text.get()
        if(pincode==""):
            messagebox.showerror("Error","Enter Pincode")
            return
        for row in database.search(self.Prop_type_text.get(), self.Pincode_text.get()):
            self.list2.insert(END, row)
    

    def get_selected_row1(self,event):   #the "event" parameter is needed b/c we've binded this function to the listbox
        try:
            index = self.list2.curselection()[0]
            self.selected_tuple = self.list2.get(index)
            self.e1.delete(0,END)
            self.e1.insert(END,self.selected_tuple[0])
            self.e2.delete(0,END)
            self.e2.insert(END,self.selected_tuple[1])
            self.e5.delete(0,END)
            self.e5.insert(END,self.selected_tuple[2])
            self.e6.delete(0,END)
            self.e6.insert(END,self.selected_tuple[3])
            self.e7.delete(0,END)
            self.e7.insert(END,self.selected_tuple[4])

          
            
        except IndexError:
            pass                #in the case where the listbox is empty, the code will not execute





    
    
        

    

#code for the GUI (front end)
#window = Tk()
#BuyerWindow(window)

#window.mainloop()
