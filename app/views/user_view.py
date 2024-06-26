from app.models.user_model import User

class UserView:
    @staticmethod
    def display_menu():
        message = '''
            ---- SISTEMA RECUPERAÇÃO DE ARTIGOS CIENTÍFICOS ----

            1 – Cadastrar Novo Usuário
            2 – Recuperar Senha
            3 – Login
            4 – Sair
        '''

        print(message)  
    
    @staticmethod
    def get_user_choice():
        choice = input('Digite uma opção: ')
        return choice
    
    @staticmethod
    def display_message(message):
        print(message)
    
    @staticmethod
    def get_user_login_info():
        CPF = input("Digite seu CPF: ")
        password = input("Digite a sua senha: ")
        return CPF, password
    
    @staticmethod
    def get_user_info():
        cpf = input("Insira seu CPF: ")
        name = input("Insira seu nome: ")
        age = int(input("Insira a sua idade: "))
        email = input("Insira seu e-mail: ")
        address = input("Insira seu endereço: ")
        password = input("Insira uma nova senha: ")
        return User(cpf, name, age, email, address, password)
        
