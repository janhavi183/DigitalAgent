from tkinter import *
from agentbackend import  AgentDAL
from tkinter import messagebox
from tkinter import ttk
from tkinter.ttk import Treeview

objAgentDAL = AgentDAL("Property.db")

class AgentWindow(object):
    def __init__(self,window):
        self.window = window
        self.window.wm_title("Agent")
        window.geometry("750x500")
        TAB_CONTROL = ttk.Notebook(window)
      
        #Tab2
        TAB2 = ttk.Frame(TAB_CONTROL)
        TAB_CONTROL.add(TAB2, text='My Inquery')

        #Tab3
        TAB3 = ttk.Frame(TAB_CONTROL)
        TAB_CONTROL.add(TAB3, text='Add Property')
        
        TAB_CONTROL.pack(expand=1, fill="both")

        #Tab3
        l1 = Label(TAB3, text="Property Type",font=('arial',10,'bold'),bd=2)
        l1.grid(row=0, column=0, pady=5)
        
        self.Prop_type_text = StringVar()
        self.e1 = Entry(TAB3, textvariable=self.Prop_type_text)
        self.e1.grid(row=0, column=1, pady=5)

        l2 = Label(TAB3, text="Pincode",font=('arial',10,'bold'),bd=2)
        l2.grid(row=0, column=2, pady=5)
        
        self.Pincode_text = StringVar()
        self.e2 = Entry(TAB3, textvariable=self.Pincode_text)
        self.e2.grid(row=0, column=3, pady=5)
        

        l3 = Label(TAB3, text="Address",font=('arial',10,'bold'),bd=2)
        l3.grid(row=1, column=0, pady=5)
        
        self.address_text = StringVar()
        self.e3 = Entry(TAB3, textvariable=self.address_text)
        self.e3.grid(row=1, column=1, pady=5)

        l4 = Label(TAB3, text="Cost",font=('arial',10,'bold'),bd=2)
        l4.grid(row=1, column=2, pady=5)
               
        self.cost_text = StringVar()
        self.e4= Entry(TAB3, textvariable=self.cost_text)
        self.e4.grid(row=1, column=3, pady=5)

        l5 = Label(TAB3, text="Email",font=('arial',10,'bold'),bd=2)
        l5.grid(row=2, column=0, pady=5)
        
        self.Email_text = StringVar()
        self.e5= Entry(TAB3, textvariable=self.Email_text)
        self.e5.grid(row=2, column=1, pady=5)

        b3 = Button(TAB3, text="Add entry",font=('arial',10,'bold'),bd=2, width=12, command=self.add_command)
        b3.grid(row=3, column=1, pady=5)
        
        
        b6 = Button(TAB3, text="Close",font=('arial',10,'bold'),bd=2, width=12, command=window.destroy)
        b6.grid(row=3, column=2, pady=5)
        
        l6 = Label(TAB3, text="My Properties")
        l6.grid(row=4, column=0, pady=5,sticky=W)
        l6.config(font=("Courier", 16))
        frame_router = Frame(TAB3)
        frame_router.grid(row=5, column=0, columnspan=4, pady=5)
        columns = ['id', 'Type', 'Pincode', 'Address', 'Cost','Email']
        router_tree_view = Treeview(frame_router, columns=columns, show="headings")
        router_tree_view.column("id", width=30)
        for col in columns[1:]:
            router_tree_view.column(col, width=140)
            router_tree_view.heading(col, text=col)
        #router_tree_view.bind('<<TreeviewSelect>>', select_router)
        router_tree_view.pack(side="left", fill="y")
        scrollbar = Scrollbar(frame_router, orient='vertical')
        scrollbar.configure(command=router_tree_view.yview)
        scrollbar.pack(side="right", fill="y")
        router_tree_view.config(yscrollcommand=scrollbar.set)
        
        for i in router_tree_view.get_children():
            router_tree_view.delete(i)
        for row in objAgentDAL.searchpropertysell():
            router_tree_view.insert('', 'end', values=row)
        
        #Tab3 End
       
        l7 = Label(TAB2, text="My Inquiry")
        l7.grid(row=0, column=0, pady=5,sticky=W)
        l7.config(font=("Courier", 16))
        frame_inquiry = Frame(TAB2)
        frame_inquiry.grid(row=1, column=0, pady=5)
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
        for row in objAgentDAL.searchInquiry():
            inquiry_tree_view.insert('', 'end', values=row)
       
    
            
    def get_selected_row(self,event):   #the "event" parameter is needed b/c we've binded this function to the listbox
        try:
            index = self.MyProperties.curselection()[0]
            self.selected_tuple = self.list1.MyProperties(index)
            self.e1.delete(0,END)
            self.e1.insert(END,self.selected_tuple[1])
            self.e2.delete(0, END)
            self.e2.insert(END,self.selected_tuple[2])
            self.e3.delete(0, END)
            self.e3.insert(END,self.selected_tuple[3])
            self.e4.delete(0, END)
            self.e4.insert(END,self.selected_tuple[4])
            self.e5.delete(0, END)
            self.e5.insert(END,self.selected_tuple[5])
            self.e6.delete(0, END)
            self.e6.insert(END,self.selected_tuple[6])
                       
            
        except IndexError:
            pass                

    def add_command(self):
        propType = self.Prop_type_text.get()
        pincode = self.Pincode_text.get()
        address = self.address_text.get()
        cost=self.cost_text.get()
        Email=self.Email_text.get()
        if(propType== ""):
            messagebox.showerror("Error","Enter Property Type")
            return
        if(pincode== ""):
            messagebox.showerror("Error","Enter Pincode")
            return
        if(address== ""):
            messagebox.showerror("Error","Enter Address")
            return
        if(cost== ""):
            messagebox.showerror("Error","Enter Cost")
            return
        if(Email== ""):
            messagebox.showerror("Error","Enter Email")
            return
        objAgentDAL.insert(propType, pincode,address, cost,Email)
        messagebox.showinfo("Messgae","Property Added Successfully")                   
   
    def get_selected_row1(self,event):   
        try:
            index = self.list2.curselection()[0]
            self.selected_tuple = self.list2.get(index)
           
            self.e9.delete(0, END)
            self.e9.insert(END,self.selected_tuple[9])
                              
        except IndexError:
            pass            

#code for the GUI (front end)
#window = Tk()
#window.geometry("400x100")
#AgentWindow(window)
#window.mainloop()
