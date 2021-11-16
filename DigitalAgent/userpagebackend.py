import sqlite3
import Session as objmanageSession
class Database:
    def __init__(self,db):
        self.conn = sqlite3.connect(db)
        self.cur = self.conn.cursor()
      

    
    def search(self,Prop_type="", Pincode=""):
        self.cur.execute("SELECT Prop_type,Pincode,address,cost,EmailAgent FROM tblProperty WHERE Prop_type = ? AND Pincode = ?",(Prop_type,Pincode))
        rows = self.cur.fetchall()
        #conn.close()
        return rows
    def insertrequirement(self,Prop_type="", Pincode="",address="",cost="",EmailAgent=""):
        #the NULL parameter is for the auto-incremented id
        Email = objmanageSession.GetSession()
        self.cur.execute("INSERT INTO tblInquiry VALUES(Null,?,?,?,?,?,?)",(Prop_type, Pincode,address,cost,Email,EmailAgent))
        self.conn.commit()
    def GetMyInquiry(self):
        Email = objmanageSession.GetSession()
        self.cur.execute("SELECT * FROM tblInquiry WHERE  Email = ? ", (Email,))
        rows = self.cur.fetchall()
        return rows

    #def view(self):
        #self.cur.execute("SELECT Prop_type,Pincode,address,cost,EmailAgent FROM tblProperty")
        #rows = self.cur.fetchall()

        #return rows

    #destructor-->now we close the connection to our database here
    def __del__(self):
        self.conn.close()
