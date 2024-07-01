import os
from datetime import datetime
import csv

class CSV:
    def __init__(self, directory):
        self.directory = directory
        if not os.path.exists(directory):
            os.makedirs(directory)
    
    def export_articles_to_csv(self, articles):
        try:
            current_time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            file_name = f"articles_{current_time}.csv"
            file_path = os.path.join(self.directory, file_name)
            with open(file_path, mode='w', newline='', encoding='utf-8') as file:
                writer = csv.writer(file, delimiter=';')
                
                writer.writerow(['ID', 'Título', 'Resumo', 'Link', 'Query'])
                
                for article in articles:
                    writer.writerow([
                        article['id'],
                        article['title'],
                        article['summary'],
                        article['link'],
                        article['query']
                    ])
            print(f"Dados exportados com sucesso para {file_path}") #debug
            return True
        except Exception as e:
            print(f"Erro ao exportar dados para CSV: {e}")  #debug
            return False
