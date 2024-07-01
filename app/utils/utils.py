import os
from datetime import datetime
import csv
import string
import random
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv

load_dotenv(dotenv_path='venv/.env')

EMAIL = os.getenv('EMAIL')
SENHA = os.getenv('SENHA')

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

class Email:
    @staticmethod
    def random_password(pass_size=5):
        characters = string.ascii_letters + string.digits + "!@#$"
        return ''.join(random.choice(characters) for _ in range(pass_size))
    
    @staticmethod
    def send_email(to, subject, message):
        msg = MIMEMultipart()
        msg['From'] = EMAIL
        msg['To'] = to
        msg['Subject'] = subject

        corpo_email = MIMEText(message, 'plain', 'utf-8')
        msg.attach(corpo_email)

        try:
            with smtplib.SMTP('smtp.gmail.com', 587) as server:
                server.starttls()
                server.login(EMAIL, SENHA)
                print(f"Enviando e-mail para: {to}")
                print(f"Assunto: {subject}")
                print(f"Mensagem: {message}")
                server.sendmail(EMAIL, to, msg.as_string())
            print("Email enviado com sucesso!")  #debug
        except Exception as e:
            print(f"email:{EMAIL} e senha:{SENHA} \n\nErro ao enviar email: {e}") #debug

