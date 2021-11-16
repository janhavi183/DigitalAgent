  
def SetSession(Email=""):
    session = open("session.txt","w") 
    session.writelines(Email) 
    session.close() #to change file access modes 

def GetSession():
    session = open("session.txt","r") 
    return session.read() 
          




