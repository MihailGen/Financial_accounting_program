from config.settings import Paths
from config.settings import Constants_and_variables
from services.transaction_management import add_transaction
from utils.file_handler import read_json
from utils.file_handler import write_json
from utils.currency_converter import converter
import asyncio

class Account:
    def __init__(self,  account_id: int, username: str, name: str, currency: int, balance: float, status=0):
        self.account_id = account_id
        self.username = username
        self.name = name
        self.currency = currency
        self.balance = balance
        self.status = status

    # Добавление дохода
    def add_income(self, amount):
        self.balance += float(amount)
        update_account_balance(self.username, self.account_id, self.balance)
        return self.balance


    # Регистрация расхода
    def add_expense(self, amount):
        if float(amount) < self.balance:
            self.balance -= amount
            update_account_balance(self.username, self.account_id, self.balance)
        else:
            print('Insufficient funds')
            return False
        return self.balance

    # Получение текущего баланса
    def get_balance(self):
        return self.balance

    # Осуществление перевода средств на другой счет
    def transfer(self, other_account, amount):
        self.add_expense(amount)
        transaction = add_transaction(self.account_id, self.username, amount, 'Payment', f"Transfer to {other_account}")
        transaction.record_transaction()
        # Узнаём, какая валюта на втором счёте
        path = Paths.path_accounts(self.username)
        data_tmp = read_json(path)
        currency_first = Constants_and_variables.currency[int(self.currency)]
        currency_two = Constants_and_variables.currency[int(data_tmp[other_account]["currency"])]
        amount_converted = asyncio.run(converter(currency_first, currency_two, amount))
        transaction = add_transaction(other_account, self.username, amount_converted, 'Income', f"Transfer from {self.account_id}")
        transaction.record_transaction()


def update_account_balance(username, account_id, balance):
    print(f"update_account_balance{username, account_id, balance}")
    path = Paths.path_accounts(username)
    data_tmp = read_json(path)
    data_tmp[account_id]["balance"] = balance
    write_json(path, data_tmp)