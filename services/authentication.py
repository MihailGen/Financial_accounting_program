# The authentication module contains functions
# for authentication and user session management
import config.settings
from config.settings import Paths
from utils.file_handler import read_json, write_json
from utils.logger import logger_events


# для входа пользователя
@logger_events("Login to system")
def login_fnc(login, password):
    data_tmp = read_json(Paths.users_json)
    if login in data_tmp:
        if (data_tmp[login][0] == hash_funct(password)):
            print("Password is correct")
            return True
        else:
            print("Password is incorrect")
            return False
    else:
        print(f"Login {login} unregistered")
        return False


# для выхода из системы,
@logger_events("Logout")
def logout_fnc(username):
    print(f"{username}! Thank you for using this program!")
    exit()


# для регистрации нового пользователя
@logger_events("Registration")
def register(username, password, email):
    try:
        data_tmp = read_json(Paths.users_json)
        if username in data_tmp:
            print(f"Login {username} already exist\ntry it again!")
            return False
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
        data_tmp[username][0] = hash_funct(password)
        data_tmp[username][1] = email
        write_json(Paths.users_json, data_tmp)
    except Exception as e:
        print(e)
        return False
    return True

# Getting user email
def user_mail_from_Json(username):
    try:
        data_tmp = read_json(Paths.users_json)
        email = data_tmp[username][1]
    except:
        return False
    return email


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
