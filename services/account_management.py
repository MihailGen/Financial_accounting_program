from models.account import Account
from utils.file_handler import read_json
from utils.file_handler import write_json
from config.settings import Paths
from pathlib import Path


import os
import json
# Управление счетами пользователей

def create_account(account_id, name, currency, balance):
    account = Account(account_id, name, currency, balance)
    read_json(Paths.path_accounts())

def save_account_to_json(login, account):
    data = {
        account.account_id: {"name": account.name,
                             "currency": account.currency,
                             "balance": account.balance
                             }
    }
    # если файла не существует, записываем в него данные сразу
    path = Paths.path_accounts(login)
    print(path)
    try:
        # if (os.stat(path).st_size == 0):
        if not os.path.isfile(Paths.path_accounts(login)):
            print("No")
            with open(path, "w", encoding="utf-8") as file:
            #     print(path + "What_happend?")
            # with open(path, "w") as write_file:
                # json.dump(data, write_file)
                path.write_text(json.dumps(data), encoding='utf-8')
            # json.dumps(data)
            # write_json(path, data)
            print("Yeeee")
                # json.dump(data, file)
        # иначе - вытаскиваем из файла структуру, дополняем её и вновь записываем
        else:
            print("Yes")
            data_tmp = read_json(Paths.path_accounts(login))
            data_tmp.update(data)
            if data_tmp:
                write_json(path, data_tmp)
            else:
                write_json(path, data)
    except FileNotFoundError:
        return False


# acc = Account(1, "Счёт в банке Цитадель", "RUB", 1000)
# save_account_to_json("mihailGen", acc)

