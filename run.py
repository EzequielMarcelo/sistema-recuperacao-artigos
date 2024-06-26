from app.controllers.user_controller import UserController
from app.database.database import Database

def main():
    userController = UserController()
    dataBase = Database('venv/Database/database.db')
    while True:
        userController.display_menu()
        choice = userController.get_user_choice()
        if choice == "1":
            userController.register_user(dataBase)
        elif choice == "2":
            userController.recover_password()
        elif choice == "3":
            userController.login_user()         
        elif choice == "4":
            break               # ends the program
        else:
            userController.display_message("Escolha Inválida")

if __name__ == "__main__":
    main()   