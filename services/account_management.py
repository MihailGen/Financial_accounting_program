# from models.account import Account
from utils.file_handler import read_json
from utils.file_handler import write_json
from config.settings import Paths
from pathlib import Path

import os
import json


# Управление счетами пользователей

def create_account(account_id, name, currency, balance):
    pass
    # account = Account(account_id, name, currency, balance)
    # read_json(Paths.path_accounts())


# write accounts to the JSON
def save_account_to_json(login, account):
    data = {
        account.account_id: {
            "username": account.username,
            "name": account.name,
            "currency": account.currency,
            "balance": account.balance,
            "status": account.status
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


def account_from_file(username, account_id):
    print(Paths.path_accounts(username))
    data_tmp = read_json(Paths.path_accounts(username))
    print(data_tmp[account_id])
    return data_tmp[account_id]


def update_account(account_id, name, currency, balance):
    pass


# rewrite balance
def update_account_balance(username, account_id, balance):
    print('Start update_account_balance')
    path = Paths.path_accounts(username)
    print(path)
    data_tmp = read_json(path)
    print(data_tmp)
    data_tmp[account_id]["balance"] = balance
    write_json(path, data_tmp)


# ID generator for accounts
def create_id_for_account(login):
    path = Paths.path_accounts(login)
    data_tmp = read_json(path)
    if not data_tmp:
        return 1
    else:
        id_account = len(data_tmp) + 1
        return id_account
