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

# write accounts to the JSON
def save_account_to_json(login, account):
    data = {
        account.account_id: {
            "name": account.name,
            "currency": account.currency,
            "balance": account.balance
        }
    }
    path = Paths.path_accounts(login)
    # если файла не существует, записываем в него данные сразу
    print(path)
    try:
        if not os.path.isfile(path):
            with open(path, "w", encoding="utf-8") as file:
                write_json(path, data)
        # иначе - вытаскиваем из файла структуру, дополняем её и вновь записываем
        else:
            data_tmp = read_json(path)
            data_tmp.update(data)
            if data_tmp:
                write_json(path, data_tmp)
            else:
                write_json(path, data)
    except FileNotFoundError:
        return False

# ID generator for accounts
def create_id_for_account(login):
    path = Paths.path_accounts(login)
    data_tmp = read_json(path)
    if not data_tmp:
        return 1
    else:
        id_account = len(data_tmp) + 1
        return id_account
