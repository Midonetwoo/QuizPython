

# import required modules 
import mysql.connector 
  
# create connection object 
con = mysql.connector.connect( 
  host="localhost", user="root", 
  password="", database="ruang_guru_kw") 
  
# create cursor object 
cursor = con.cursor() 

class user:
    
    def __init__(self,id ,username, password):
        self.__id = id
        self.__username = username
        self.__password = password

    def intro(self):
        print("id = ",self.__id)
        print("username = ",self.__username)
        print("password = ",self.__password)

    def signUp(self):
        self.__username = input("masukkan username > ")
        self.__password = input("masukkan password > ")
        
        
        query = f"select * from tbuser "
        cursor.execute(query)
        
        result = cursor.fetchall()
        
        for i in result:
            if i[1] == self.__username: 
                print("username telah digunakan")
                break
                
            else:
                data = [(self.__username,self.__password)]
                query = "insert into tbuser (username, password) values (%s, %s)"
                
                cursor.executemany(query, data)
                
                # untuk mengubah data di database
                con.commit()
                
                print("Berhasil Sign Up")
                
        
        
        
    def login(self):
        self.__username = input("masukkan username > ")
        self.__password = input("masukkan password > ")
        
        query = f"select * from tbuser "
        cursor.execute(query)
        
        result = cursor.fetchall()
        
        for i in result:
            if i[1] == self.__username and i[2] == self.__password:
                self.__id = i[0] 
                print("username ditemukan")
                break
                
            else:
                continue
                
    

    
