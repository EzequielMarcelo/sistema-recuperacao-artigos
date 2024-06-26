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
        cep = input("Insira seu CEP (apenas numeros): ")
        password = input("Insira uma nova senha: ")
        return cpf, name, age, email, cep, password
    
    @staticmethod
    def get_user_address_manually(cep):
        print('Endereco nao encontrado!')
        patio = input("Digite o logradouro: ")
        neighborhood = input("Digite o bairro: ")
        city = input("Digite a cidade: ")
        state = input("Digite a sigla do estado: ")
        full_address = f"{patio}, {neighborhood}, {cep}, {city}, {state}"
        return full_address
        
