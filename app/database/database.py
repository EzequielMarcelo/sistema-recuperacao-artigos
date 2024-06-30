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
        self.vectorizer_max_features = 200
        self.vectorizer = TfidfVectorizer(max_features=self.vectorizer_max_features)

    def connect_to_collection(self, cpf):
        collection_name = f"colect_{cpf}"
        try:
            collection = self.client.get_or_create_collection(name=collection_name)
            return collection
        except Exception as e:
            print(f"Error connecting to collection {collection_name}: {e}")       
            return None
        
    def train_vectorizer(self, documents):
        self.vectorizer.fit(documents)
        print(f"Vectorizer trained with {len(documents)} documents.")

    def index_document(self, collection, doc_id, summary):
        try:
            if self.vectorizer is None:
                raise ValueError("Vectorizer is not trained.")
                
            summary_vector = self.vectorizer.transform([summary])
            embeddings = summary_vector.toarray().tolist()[0] 
            if len(embeddings) < self.vectorizer_max_features:
                embeddings.extend([0] * (self.vectorizer_max_features - len(embeddings)))
            else:
                embeddings = embeddings[:self.vectorizer_max_features]
                
            collection.upsert(
                ids=[doc_id],
                embeddings=[embeddings]
            )
            print(f"Document '{doc_id}' successfully indexed in the collection.")
            return True
        except Exception as e:
            print(f"Error when indexing document: {e}")
            return False

    def search_documents(self, collection, query, max_results):
        try:
            query_vector = self.vectorizer.transform([query]).toarray().tolist()
            
            results = collection.query(
                query_embeddings=query_vector,
                n_results=max_results  
            )
            return results
        except Exception as e:
            print(f"Error searching for documents: {e}")
            return None
         