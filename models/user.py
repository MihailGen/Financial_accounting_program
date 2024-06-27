from utils import file_handler
from services import authentication


class User:

    def __init__(self,  username,  password, email):
        self.username = username
        self.password = password
        self.email = email

    # Регистрация пользователя
    def register(self):
        print("Start registr")
        # подготовка словаря для добавления в файл пользователя
        # пароль хэшируем
        data = {
            self.username: [authentication.hash_funct(self.password),  self.email],
            }
        # запуск функции добавления в файл пользователя
        try:
         file_handler.user_to_datafile(data)
        except:
            print("Ошибка записи в файл")
        print(
                "\n*************\nCongratulation!!!\nYou have successfully created new account\nYour login:  " + self.username + "\n")


    # для входа в систему
    def login(self, username, password):
        file_handler.login(data)

    # для обновления профиля пользователя
    def update_profile(self):
        pass
