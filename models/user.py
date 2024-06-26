from utils import file_handler
from services import authentication


class User:

    def __init__(self,  username,  password, email):
        self.username = username
        self.password = password
        self.email = email

    # Регистрация пользователя
    def register(self):
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
    def login(self, login, pswd):
        if check_log(login):
            try:
                with open('bank_clients/' + login + '.' + 'passwordhash.txt') as file_hash:
                    if hash_funct(passw) == file_hash.readline():
                        file_hash.close()
                    else:
                        print('\n*************\nIncorrect password')
                        return False
            except FileNotFoundError:
                print('A system error has occurred!\n Please contact an administrator.\n')
                return False
            return True
        else:
            return False

    # для обновления профиля пользователя
    def update_profile(self):
        pass
