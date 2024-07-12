#  Модуль authentication содержит функции
#  для аутентификации и управления сессиями пользователей

import config.settings
from config.settings import Paths
from utils.file_handler import read_json
from utils.file_handler import write_json
from utils.logger import logger_events


# для входа пользователя
@logger_events("Login to system")
def login_fnc(login, password):
    data_tmp = read_json(Paths.users_json)
    if login in data_tmp:
        if (data_tmp[login][0] == hash_funct(password)):
            print("Password is correct")
        else:
            return False
    else:
        return False
    return True


# для выхода из системы,
@logger_events("Logout")
def logout_fnc(username):
    print(f"Good by {username}!")
    exit()


# для регистрации нового пользователя
@logger_events("Registration")
def register(username, password, email):
    try:
        data_tmp = read_json(Paths.users_json)
        data = {
            username: [hash_funct(password), email],
        }
        data_tmp.update(data)
        write_json(Paths.users_json, data_tmp)
    except Exception as e:
        print(e)
        return False
    return True

def update_user_information(username, password, email):
    try:
        data_tmp = read_json(Paths.users_json)
        data = {
            username: [hash_funct(password), email],
        }

        data_tmp[username][0] = hash_funct(password)
        data_tmp[username][1] = email
        write_json(Paths.users_json, data_tmp)
    except Exception as e:
        print(e)
        return False
    return True





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
