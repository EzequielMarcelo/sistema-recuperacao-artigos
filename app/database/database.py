import os
import sqlite3
from app.models.user_model import User

class Database:
    def __init__(self, data_base_path):
            self.data_base_path = data_base_path
            directory = os.path.dirname(data_base_path)
            
            if not os.path.exists(directory):
                os.makedirs(directory, exist_ok=True)

            if not os.path.exists(data_base_path):
                self.create_tables()

    def create_tables(self):
        connection = sqlite3.connect(self.data_base_path)
        cursor = connection.cursor()        

        cursor.execute('''CREATE TABLE IF NOT EXISTS User (
                            cpf VARCHAR(14) NOT NULL PRIMARY KEY,
                            name TEXT NOT NULL,
                            age INTEGER,
                            email TEXT,
                            address TEXT,
                            password TEXT)''')
        
        cursor.execute('''CREATE TABLE IF NOT EXISTS Article (
                            id TEXT PRIMARY KEY,
                            title TEXT NOT NULL,
                            summary TEXT NOT NULL,
                            link TEXT NOT NULL,
                            user_cpf VARCHAR(14) NOT NULL,
                            query TEXT NOT NULL,
                            FOREIGN KEY (user_cpf) REFERENCES User (cpf))''')
        
        connection.commit()
        connection.close()
    
    def add_user(self, user: User):
            connection = sqlite3.connect(self.data_base_path)
            cursor = connection.cursor()
            cursor.execute('''INSERT INTO User (cpf, name, age, email, address, password)
                            VALUES (?, ?, ?, ?, ?, ?)''', 
                            [user.cpf, user.name, user.age, user.email, user.address, user.password])
            
            connection.commit()
            connection.close()

    def search_user(self, cpf):
        connection = sqlite3.connect(self.data_base_path)
        cursor = connection.cursor()        
       
        cursor.execute("SELECT * FROM User WHERE cpf = ?", (cpf,))
        user = cursor.fetchone()
        
        connection.close()
        
        if user:
            user_model = User(
                user[0],
                user[1],
                user[2],
                user[3],
                user[4],
                user[5]
            )
            return user_model
        else:
            return None
         
         