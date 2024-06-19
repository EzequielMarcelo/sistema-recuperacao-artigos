from app.controllers.main_controller import MainController
from app.views.main_view import MainView

def main():
    controller = MainController()
    while True:
        MainView.display_menu()
        choice = MainView.get_user_choice()
        if choice == "1":
            controller.register_user()
        elif choice == "2":
            controller.recover_password()
        elif choice == "3":
            controller.login_user()
        elif choice == "4":
            break               # ends the program
        else:
            MainView.display_message("Escolha Inválida")

if __name__ == "__main__":
    main()   