from app.views.main_view import MainView

class MainController:
    def __init__(self):
        self.view = MainView()

    def register_user(self):
        self.view.display_message("Voce escolheu a opcao 1")

    def recover_password(self):
        self.view.display_message("Voce escolheu a opcao 2")

    def login_user(self):
        self.view.display_message("Voce escolheu a opcao 3")