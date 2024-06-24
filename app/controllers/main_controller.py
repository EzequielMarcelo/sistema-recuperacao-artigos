from app.views.main_view import MainView
from app.controllers.article_controller import ArticleController

class MainController:
    def __init__(self):
        self.view = MainView()
        self.article_controller = ArticleController()
    
    def display_menu(self):
        self.view.display_menu()
    
    def get_user_choice(self):
        return self.view.get_user_choice()
    
    def display_message(self, message):
        self.view.display_message(message)

        
    def register_user(self):
        self.view.display_message("Voce escolheu a opcao 1")

    def recover_password(self):
        self.view.display_message("Voce escolheu a opcao 2")

    def login_validate(self, CPF, password):
        return True
    
    def login_user(self):
        CPF, password = self.view.get_user_login_info()
        is_validate = self.login_validate(CPF, password)
       
        if not is_validate:
            self.view.display_message('Senha ou CPF inválidos')
            return
        
        while True:
                self.article_controller.display_menu()
                choice = self.article_controller.get_user_choice()
                if choice == "1":
                    self.article_controller.display_message("BUSCA ARXIV")
                elif choice == "2":
                    self.article_controller.display_message("BUSCA COLEÇÃO ARTIGOS")
                elif choice == "3":
                    self.article_controller.display_message("LISTAR ARTIGOS")
                elif choice == "4":
                    break
                else:
                    self.article_controller.display_message("Opção inválida.")

        

        

    
    

        