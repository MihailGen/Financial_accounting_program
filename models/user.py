from utils import file_handler
from services import authentication


class User:

    def __init__(self,  username,  password, email):
        self.username = username
        self.password = password
        self.email = email

    # Регистрация пользователя
    def register(self):
        authentication.register(self.username, self.password, self.email)
        print("\n*************\nCongratulation!!!\nYou have successfully created new account\nYour login:  " + self.username + "\n")


    # для входа в систему
    def login(self):
        authentication.login(self.username, self.password)

    # для обновления профиля пользователя
    def update_profile(self):
        pass
