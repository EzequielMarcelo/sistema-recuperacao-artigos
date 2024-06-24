from app.controllers.main_controller import MainController

def main():
    mainController = MainController()
    while True:
        mainController.display_menu()
        choice = mainController.get_user_choice()
        if choice == "1":
            mainController.register_user()
        elif choice == "2":
            mainController.recover_password()
        elif choice == "3":
            mainController.login_user()         
        elif choice == "4":
            break               # ends the program
        else:
            mainController.display_message("Escolha Inválida")

if __name__ == "__main__":
    main()   