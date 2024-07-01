from app.views.user_view import UserView
from app.controllers.article_controller import ArticleController
from app.database.database import Database
from app.models.user_model import User
from app.utils.utils import Email, CEP

class UserController:
    def __init__(self, database:Database):
        self.database = database 
        self.view = UserView()
        self.article_controller = ArticleController(database)
    
    def display_menu(self):
        self.view.display_menu()
    
    def get_user_choice(self):
        return self.view.get_user_choice()
    
    def display_message(self, message):
        self.view.display_message(message)
        
    def register_user(self):
        cpf, name, age, email, cep, password = self.view.get_user_info()
        address = CEP.get_address_by_cep(cep)
        
        if address is None:
            address = self.view.get_user_address_manually(cep)
        
        user = User(cpf, name, age, email, address, password)
        self.database.add_user(user)

    def recover_password(self):
        email = self.view.get_info_recover_password()
        user = self.database.search_user_by_email(email)
        if user:
            new_pass = Email.random_password()
            self.database.update_password(user.cpf, new_pass)
            message = f"Oi {user.name}, sua nova senha é {new_pass}."
            Email.send_email(email, "Recuperação de Senha", message)
        else:
            print("E-mail não cadastrado.")

    def login_validate(self, CPF, password):
        valid_cpf = False
        valid_password = False
        user = self.database.search_user(CPF)
           
        if user is not None:
            valid_cpf = True
            if user.password == password:
                valid_password = True

        return valid_cpf, valid_password, user
    
    def login_user(self):
        CPF, password = self.view.get_user_login_info()
        valid_cpf, valid_password, current_user = self.login_validate(CPF, password)

        if not valid_cpf and not valid_password:
            self.view.display_message('Usuario nao encontrado')
            return
        
        if not valid_password:
            self.view.display_message('Senha inválida')
            return 

        self.article_controller.set_current_user(current_user)          
        
        while True:
                self.article_controller.display_menu()
                choice = self.article_controller.get_user_choice()
                if choice == "1":
                    self.article_controller.arxiv_search()
                elif choice == "2":
                    self.article_controller.browse_article_collection()
                elif choice == "3":
                    self.article_controller.display_all_articles()
                elif choice == "4":
                    break
                else:
                    self.article_controller.display_message("Opção inválida.")

        

        

    
    

        