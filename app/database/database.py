import os
import sqlite3
from app.models.user_model import User
import chromadb
from sklearn.feature_extraction.text import TfidfVectorizer

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
        
    def add_article(self, article_data):
        connection = sqlite3.connect(self.data_base_path)
        cursor = connection.cursor()  

        cursor.execute('SELECT 1 FROM Article WHERE id = ?', (article_data[0],))
        
        if not cursor.fetchone():
            cursor.execute('''
                INSERT INTO Article (id, title, summary, link, user_cpf, query)
                VALUES (?, ?, ?, ?, ?, ?)
            ''', article_data)

        connection.commit()
        connection.close()  

class ChromaDB:
    def __init__(self, storage_path):
        self.storage_path = storage_path
        self.client = chromadb.PersistentClient(path=storage_path)
        self.vectorizer = TfidfVectorizer(max_features=10)

    def connect_to_collection(self, cpf):
        collection_name = f"colect_{cpf}"
        try:
            collection = self.client.get_or_create_collection(name=collection_name)
            return collection
        except Exception as e:
            # debug print(f"Error connecting to collection {collection_name}: {e}")       
            return None

    def index_document(self, collection, doc_id, summary):
        try:
            summary_vector = self.vectorizer.fit_transform([summary])
            embeddings = summary_vector.toarray().tolist()

            collection.upsert(
                ids=[doc_id],
                embeddings=embeddings
            )
            # debug print(f"Document '{doc_id}' successfuly indexed in the collection.")
            return True
        except Exception as e:
            # debug print(f"Error when idexing document: {e}")
            return False

    def search_documents(self, collection, query):
        try:
            query_vector = self.vectorizer.transform([query])
            query_embeddings = query_vector.toarray().tolist()

            results = collection.query(
                query_embeddings=query_embeddings,
            )
            return results
        except Exception as e:
            # debugprint(f"Error searching for documents: {e}")
            return None         
         