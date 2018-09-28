#import sqlite3
import pymysql as sql

class Database():

    def __init__(self):
        self.connect = sql.connect("localhost",'root','','rail')
        self.connectCursor = self.connect.cursor()
    
    def getDBConnection(self,ip="localhost",username="root",password="",dbname="rail"):
        try:
            db=sql.connect(ip,username,password,dbname)
            cursor=db.cursor()
        except BaseException as e:
            print(e)
        else:
            print("connection done successfully!!")
        return(db,cursor)


    def LoginUser(self, user_email, user_password):
        self.connect,self.connectCursor = self.getDBConnection()
        query = "SELECT COUNT(*) from user_details where user_email='%s' AND user_password='%s'"%(user_email,user_password)
        self.connectCursor.execute(query)
        if (self.connectCursor.fetchall())[0][0]>0:
            return "User Found."
        else:
            return "User Does Not Exists."
        self.connect.commit()
        self.connect.close()

    def UserDetails(self):
        self.connect,self.connectCursor =self.getDBConnection()
        query = "SELECT * FROM user_details"
        self.connectCursor.execute(query)
        result=self.connectCursor.fetchall()
        self.connect.close()
        return result
	
    def Insert(self,name,age,Phone_number,email_address,paasword,gender):
        connect,connectCursor = self.getDBConnection(self)
        try:
            a=(name,age,Phone_number,email_address,paasword,gender)
            query="insert into user_details (`name`,`Age`,`mobile_no`,`user_email`,`user_password`,`Gender`) values "+str(a)
            print(query)
            connectCursor.execute(query)
            if connectCursor.rowcount==1:
                connect.commit()
            else:
                raise("some issue while insertion")
        except BaseException as e:
            connect.rollback()
            print(e)
        else:
            print("data inserted successfully!!")
        connect.close()
		

