import sqlite3
import Session as objmanageSession

class AgentDAL:
    def __init__(self,db):
        self.conn = sqlite3.connect(db)
        self.cur = self.conn.cursor()
  
    def insert(self,Prop_type, Pincode, address, cost,Email):
        EmailAgent = objmanageSession.GetSession()
        self.cur.execute("INSERT INTO tblProperty VALUES(NULL,?,?,?,?,?,?)", (Prop_type,Pincode, address, cost,Email,EmailAgent))
        self.conn.commit()
        
    def searchInquiry(self):
        EmailAgent = objmanageSession.GetSession()
        self.cur.execute("SELECT * FROM tblInquiry WHERE EmailAgent = ? ",(EmailAgent,))
        rows = self.cur.fetchall()
        return rows
        
    def searchpropertysell(self):
        EmailAgent = objmanageSession.GetSession()
        self.cur.execute("SELECT * FROM tblProperty WHERE  EmailAgent = ? ", (EmailAgent,))
        rows = self.cur.fetchall()
        return rows
  
    def __del__(self):
        self.conn.close()
