from models.account import Account
from utils.file_handler import read_json
from utils.file_handler import write_json
from config.settings import Paths
from utils.logger import logger_events
import re
import os


# Управление счетами пользователей

@logger_events("Create account")
def create_account(username, name, currency, balance):
    account = Account(create_id_for_account(username), username, name, currency, balance)
    save_account_to_json(username, account)


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
    data_tmp = read_json(Paths.path_accounts(username))
    return data_tmp[account_id]


def update_account(account_id, name, currency, balance):
    pass


def isValid(email):
    regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')
    if re.fullmatch(regex, email):
        print("Valid email")
        return True
    else:
        print("Invalid email")
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


def check_if_account_exists(id, login):
    path = Paths.path_accounts(login)
    data_tmp = read_json(path)
    if not data_tmp:
        return False
    else:
        try:
            if data_tmp[str(id)]:
                return True
        except:
            return False


def account_proof(username):
    while True:
        try:
            while True:
                account_id = int(input("Enter the account ID: "))
                if not check_if_account_exists(str(account_id), username):
                    print(f"Account with ID {account_id} not exist")
                else:
                    break
            break
        except ValueError:
            print("Not correct number, please try again")
    return account_id


def create_account_object_from_json(login, account_id):
    path = Paths.path_accounts(login)
    data_tmp = read_json(path)
    print(data_tmp)
    if not data_tmp:
        print("Account not exist")
        return False
    else:
        try:
            if data_tmp[account_id]:
                print(data_tmp[account_id])
                acc_name = data_tmp[account_id]['name']
                print("acc_name")
                acc_currency = data_tmp[account_id]['currency']
                acc_balance = data_tmp[account_id]['balance']
                acc_status = data_tmp[account_id]['status']
                account = Account(account_id, login, acc_name, acc_currency, acc_balance, acc_status)
                return account
        except:
            print("Acc@@@@@@@")
            return False
