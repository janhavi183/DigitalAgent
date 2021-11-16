import sqlite3
import Session as objmanageSession

class Database:
    def __init__(self,db):
        self.conn = sqlite3.connect(db)
        self.cur = self.conn.cursor()
      

    def InsertProperty(self,Prop_type, Pincode, address, cost,EmailAgent):
        #the NULL parameter is for the auto-incremented id
        Email = objmanageSession.GetSession()
        self.cur.execute("INSERT INTO tblProperty VALUES(NULL,?,?,?,?,?,?)", (Prop_type,
                                                Pincode, address, cost,Email,EmailAgent))
        self.conn.commit()
    def GetAgents(self,Pincode=""):
        RoleId = "Agent"
        self.cur.execute("SELECT Name,Contact,Email FROM tblUser WHERE  Pincode = ? and RoleId = ? ", (Pincode, RoleId))
        rows = self.cur.fetchall()
        #conn.close()
        return rows
        
    def GetMyProperty(self):
        Email = objmanageSession.GetSession()
        self.cur.execute("SELECT * FROM tblProperty WHERE  Email = ? ", (Email,))
        rows = self.cur.fetchall()
        return rows


        #destructor-->now we close the connection to our database here
    def __del__(self):
        self.conn.close()

