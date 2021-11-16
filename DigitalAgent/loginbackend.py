import sqlite3
class Database:
    def __init__(self,db):
        self.conn = sqlite3.connect(db)
        self.cur = self.conn.cursor()

        
    def doLogin(self,Email="", Password=""):
        self.cur.execute("SELECT ID,RoleID FROM tblUser WHERE  Email=? and Password=?",(Email, Password))
        rows = self.cur.fetchall()
        #rows =  len(data)
        #conn.close()
        return rows
         
    

    #destructor-->now we close the connection to our database here
    def __del__(self):
        self.conn.close()

