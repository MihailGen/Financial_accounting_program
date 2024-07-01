#  Модуль authentication содержит функции
#  для аутентификации и управления сессиями пользователей

import config.settings
from config.settings import Paths
from utils.file_handler import read_json
from utils.file_handler import write_json


# для входа пользователя
def login(login, password):
    data_tmp = read_json(Paths.users_json)
    if login in data_tmp:
        print(login)
        if (data_tmp[login][0] == hash_funct(password)):
            print("Password is correct")
        return login
    else:
        return False


# для выхода из системы,
def logout():
    pass


# для регистрации нового пользователя.
def register(username, password, email):
    data_tmp = read_json(Paths.users_json)
    data = {
        username: [hash_funct(password), email],
    }
    data_tmp.update(data)
    write_json(Paths.users_json, data_tmp)


# Create Hash for password
def hash_funct(pswd):
    summ = 0
    mult = 1
    for i in range(len(pswd)):
        summ += ord(pswd[i])
        mult = mult * ord(pswd[i])
    summ = summ % config.settings.CONST_FOR_HASH
    mult = mult % config.settings.CONST_FOR_HASH
    return str(summ) + str(mult)

# path_new = Paths()
# path_new.path_accounts("MisaGen")
