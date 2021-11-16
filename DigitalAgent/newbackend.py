import sqlite3
class Database:
    def __init__(self,db):
        self.conn = sqlite3.connect(db)
        self.cur = self.conn.cursor()
      

    def insertUser(self,Name,Contact,Email,Password,RoleId,Pincode):
        #the NULL parameter is for the auto-incremented id
        self.cur.execute("INSERT INTO tblUser VALUES(NULL,?,?,?,?,?,?)",(Name,Contact,Email,Password,RoleId,Pincode))
        self.conn.commit()
    

    #destructor-->now we close the connection to our database here
    def __del__(self):
        self.conn.close()

