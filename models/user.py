from services.authentication import update_user_information
from utils import file_handler
from services import authentication


class User:

    def __init__(self,  username,  password, email):
        self.username = username
        self.password = password
        self.email = email

    # Регистрация пользователя


    def register(self):
        if authentication.register(self.username, self.password, self.email):
            print("\n*************\nCongratulation!!!\nYou have successfully created new account\nYour login:  " + self.username + "\n")
            return True
        else:
            return False



    # для входа в систему
    def login(self):
        if authentication.login_fnc(self.username, self.password):
            return True
        else:
            return False



    # для обновления профиля пользователя
    def update_profile(self, new_password, new_email):
        if update_user_information(self.username, new_password, new_email):
            return True
        else:
            return False

