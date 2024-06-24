class ArticleView:
    @staticmethod
    def display_menu():
        message = '''
            ---- SISTEMA RECUPERAÇÃO DE ARTIGOS CIENTÍFICOS ----

            1 – Realizar busca ARXIV
            2 – Realizar busca coleção de Artigos
            3 – Listar Artigos
            4 – Voltar ao Menu principal
        '''

        print(message)  
    
    @staticmethod
    def get_user_choice():
        choice = input('Digite uma opção: ')
        return choice
    
    @staticmethod
    def display_message(message):
        print(message)
