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
    
    @staticmethod
    def display_article(article):
        print("\n==== ID ====")
        print(f"{article['id']}")
        print("==== Titulo ====")
        print(f"{article['title']}")
        print("==== Resumo ====")
        print(f"{article['summary']}")
        print("==== Link ====")
        print(f"{article['id']}\n")

    @staticmethod
    def get_search_parameters():
        query = input('Digite a busca: ')
        max_results = int(input('Insira o numero maximo para a busca: '))
        return query, max_results
    
    @staticmethod
    def get_csv_export():
        choice = input('Deseja exportar os dados em CSV? S/N: ')
        success = choice.upper() == 'S'
        return success