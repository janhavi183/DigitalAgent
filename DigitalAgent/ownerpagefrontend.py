from tkinter import *
from ownerpagebackend import  Database
from tkinter import messagebox
from tkinter.ttk import Treeview
database = Database("Property.db")

class OwnerWindow(object):
    def __init__(self,window):
        self.window = window
        window.geometry("750x500")
        self.window.wm_title("Owner")

        l1 = Label(window, text="Property type",font=('arial',10,'bold'),bd=2)
        l1.grid(row=0, column=0,pady=5,sticky=W)
        
        self.Prop_type_text = StringVar()
        self.e1 = Entry(window, textvariable=self.Prop_type_text)
        self.e1.grid(row=0, column=1,pady=5,sticky=W)

        l2 = Label(window, text="Pincode",font=('arial',10,'bold'),bd=2)
        l2.grid(row=0, column=2 ,pady=5,sticky=W)   
        
        self.Pincode_text = StringVar()
        self.e2 = Entry(window, textvariable=self.Pincode_text)
        self.e2.grid(row=0, column=3 ,pady=5,sticky=W)

        b7= Button(window, text="Get Agents list",font=('arial',10,'bold'),bd=2, width=12, command=self.GetAgents)
        b7.grid(row=0, column=4,sticky=W)
        
        l3 = Label(window, text="Address",font=('arial',10,'bold'),bd=2)
        l3.grid(row=1, column=0,pady=5,sticky=W)
        
        self.address_text = StringVar()
        self.e3 = Entry(window, textvariable=self.address_text)
        self.e3.grid(row=1, column=1,pady=5,sticky=W)
        
        l4 = Label(window, text="Cost",font=('arial',10,'bold'),bd=2)
        l4.grid(row=1, column=2,pady=5,sticky=W)
        
        self.cost_text = StringVar()
        self.e4= Entry(window, textvariable=self.cost_text)
        self.e4.grid(row=1, column=3 ,pady=5,sticky=W)
        
        
        self.EmailAgent_text = StringVar()
        self.e44 = Entry(window, textvariable=self.EmailAgent_text)
        self.e44.grid(row=1, column=4,pady=5,sticky=W)
        
    
       
        l10 = Label(window, text="Agent",font=('arial',10,'bold'),bd=2)
        l10.grid(row=2, column=0 ,pady=5,sticky=W)
        
        self.list2 = Listbox(window, height=3, width=70)
        self.list2.grid(row=2, column=1 ,pady=5,columnspan=3,sticky=W)

        self.list2.bind('<<ListboxSelect>>', self.get_selected_row1)

           
        sb2 = Scrollbar(window)
        sb2.grid(row=2, column=4,pady=5,sticky=W)
        self.list2.config(yscrollcommand=sb2.set)
        sb2.config(command=self.list2.yview)
       
        b3 = Button(window, text="Upload property",font=('arial',10,'bold'),bd=2, width=12, command=self.add_command)
        b3.grid(row=3, column=1,pady=5,sticky=W)

        b6 = Button(window, text="Close",font=('arial',10,'bold'),bd=2, width=12, command=window.destroy)
        b6.grid(row=3, column=2,pady=5,sticky=W)

        l7 = Label(window, text="My Property")
        l7.grid(row=4, column=0, pady=5,sticky=W)
        l7.config(font=("Courier", 16))
        frame_inquiry = Frame(window)
        frame_inquiry.grid(row=5, column=0, pady=5,columnspan=5)
        columns = ['id', 'Type', 'Pincode', 'Address', 'Cost','Email']
        inquiry_tree_view = Treeview(frame_inquiry, columns=columns, show="headings")
        inquiry_tree_view.column("id", width=30)
        for col in columns[1:]:
            inquiry_tree_view.column(col, width=140)
            inquiry_tree_view.heading(col, text=col)
        
        inquiry_tree_view.pack(side="left", fill="y")
        scrollbar = Scrollbar(frame_inquiry, orient='vertical')
        scrollbar.configure(command=inquiry_tree_view.yview)
        scrollbar.pack(side="right", fill="y")
        inquiry_tree_view.config(yscrollcommand=scrollbar.set)
        
        for i in inquiry_tree_view.get_children():
            inquiry_tree_view.delete(i)
        for row in database.GetMyProperty():
            inquiry_tree_view.insert('', 'end', values=row)
        
    def add_command(self):
        database.InsertProperty(self.Prop_type_text.get(), self.Pincode_text.get(),
                        self.address_text.get(), self.cost_text.get(),
                        self.EmailAgent_text.get())
        messagebox.showinfo("Messgae","Property Added Successfully")   
   

    def GetAgents(self):
        self.list2.delete(0, END)
        pincode = self.Pincode_text.get()
        if(pincode==""):
            messagebox.showerror("Error","Enter Pincode")
            return
        for row in database.GetAgents(pincode):
            self.list2.insert(END, row)
            
    def get_selected_row1(self,event):   #the "event" parameter is needed b/c we've binded this function to the listbox
        try:
            index = self.list2.curselection()[0]
            self.selected_tuple = self.list2.get(index)
            self.e44.delete(0,END)
            self.e44.insert(END,self.selected_tuple[2])
          
            
        except IndexError:
            pass                #in the case where the listbox is empty, the code will not execute


#code for the GUI (front end)
#window = Tk()
#OwnerWindow(window)
#window.mainloop()
