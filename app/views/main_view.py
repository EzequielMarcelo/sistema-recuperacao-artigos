class MainView:
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