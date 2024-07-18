from models.account import Account
from utils.file_handler import read_json
from utils.file_handler import write_json
from config.settings import Paths
from pathlib import Path
from utils.logger import logger_events
import re
import os
import inspect


# Управление счетами пользователей

@logger_events("Create account")
def create_account(username, name, currency, balance):
    account = Account(create_id_for_account(username), username, name, currency, balance)
    save_account_to_json(username, account)
    return account


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
    # for test only
    try:
        if inspect.stack()[2][3] == '_callTestMethod':
            path = Path("../data/accounts/mm_accounts.json")
    except:
        path = Paths.path_accounts(login)

    # if the file does not exist, write the data to it immediately
    try:
        if not os.path.isfile(path) or os.stat("file").st_size == 0:
            with open(path, "w", encoding="utf-8") as file:
                write_json(path, data)
        # otherwise, we extract the structure from the file, supplement it and write it again
        else:
            data_tmp = read_json(path)
            data_tmp.update(data)
            if data_tmp:
                write_json(path, data_tmp)
            else:
                write_json(path, data)
    except FileNotFoundError:
        return False
    return True


# def account_from_file(username, account_id):
#     # for test only
#     if inspect.stack()[2][3] == '_callTestMethod':
#         data_tmp = read_json(Path("../data/accounts/mm_accounts.json"))
#     else:
#         data_tmp = read_json(Paths.path_accounts(username))
#     return data_tmp[account_id]

@logger_events("Update account")
def update_account(username, account_id, name, currency, balance):
    account = create_account_object_from_json(username, account_id)
    account.name = name
    account.currency = currency
    account.balance = balance
    save_account_to_json(username, account)


def is_correct_email(email):
    regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')
    if re.fullmatch(regex, email):
        print("Valid email")
        return True
    else:
        print("Invalid email")
        return False

def is_correct_amount(amount):
    regex = re.compile(r"(\d*(\.\d)?(\d)?)")
    if re.fullmatch(regex, amount):
        return True
    else:
        print("Invalid amount")
        return False

# rewrite balance
def update_account_balance(username, account_id, balance):
    path = Paths.path_accounts(username)
    data_tmp = read_json(path)
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


def check_if_account_exists(account_id, login):
    path = Paths.path_accounts(login)
    # for test only
    if inspect.stack()[2][3] == '_callTestMethod':
        path = Path("../data/accounts/mm_accounts.json")
    data_tmp = read_json(path)
    if not data_tmp:
        return False
    else:
        try:
            if data_tmp[account_id]:
                if data_tmp[account_id]['status'] == 1:
                    print("the account was deleted! Try another!\n")
                    return False
                return True
        except:
            return False


def account_proof(username, message_str):
    while True:
        try:
            while True:
                account_id = int(input(message_str))
                if not check_if_account_exists(str(account_id), username):
                    return False
                else:
                    break
            break
        except ValueError:
            print("Not correct number, please try again")
    return str(account_id)


def create_account_object_from_json(username, account_id):
    path = Paths.path_accounts(username)

    # for test only
    try:
        if inspect.stack()[2][3] == '_callTestMethod':
            path = Path("../data/accounts/mm_accounts.json")
    except Exception as e:
        path = Paths.path_accounts(username)

    data_tmp = read_json(path)
    if not data_tmp:
        print("Account not exist")
        return False
    else:
        try:
            if data_tmp[account_id]:
                acc_name = data_tmp[account_id]['name']
                acc_currency = int(data_tmp[account_id]['currency'])
                acc_balance = float(data_tmp[account_id]['balance'])
                if data_tmp[account_id]['status'] == '1':
                    print("Account deleted!")
                    return False
                else:
                    acc_status = data_tmp[account_id]['status']
                account = Account(account_id, username, acc_name, acc_currency, acc_balance, acc_status)
                return account
        except:
            print("Account not exist")
            return False
