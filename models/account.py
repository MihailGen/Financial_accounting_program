from config.settings import Paths, Constants_and_variables
from services.transaction_management import add_transaction
from utils.file_handler import write_json, read_json, update_account_balance, update_account_status
from utils.logger import logger_for_Account
from utils.currency_converter import converter
from functools import wraps
import asyncio
import os
from pathlib import Path



class Account:
    def __init__(self, account_id: int, username: str, name: str, currency: int, balance: float, status=0):
        self.account_id = account_id
        self.username = username
        self.name = name
        self.currency = currency
        self.balance = balance
        self.status = status

    # Adding Income
    @logger_for_Account("Addition income to account")
    def add_income(self, amount):
        self.balance += round(float(amount), 2)
        update_account_balance(self.username, self.account_id, self.balance)
        return self.balance

    # Expense registration
    @logger_for_Account("Register expense from account")
    def add_expense(self, amount):
        if float(amount) < self.balance:
            self.balance -= round(float(amount), 2)
            update_account_balance(self.username, self.account_id, self.balance)
        else:
            print('Insufficient funds')
            return False
        return self.balance

    # Getting the current balance
    @logger_for_Account("Get balance")
    def get_balance(self):
        return self.balance

    @logger_for_Account("Delete account")
    def delete_account(self):
        self.status = 1
        return (update_account_status(self.username, self.account_id, self.status))


    # Transferring funds to another account
    def transfer(self, other_account, amount):
        # Create expense transaction from the first account
        transaction = add_transaction(self.account_id, self.username, amount, 'Payment', f"Transfer to {other_account}")
        transaction.record_transaction()

        # Find out what currency is on the first and second account
        path = Paths.path_accounts(self.username)
        try:
            if (os.stat(path).st_size == 0):
                return False
        except FileNotFoundError:
            print("FileNotFoundError")
            path = Path("../data/accounts/mm_accounts.json")


        data_tmp = read_json(path)
        currency_first = Constants_and_variables.currency[int(self.currency)]
        currency_two = Constants_and_variables.currency[int(data_tmp[other_account]["currency"])]

        # Convert amount from currency_first to currency_two
        amount_converted = asyncio.run(converter(currency_first, currency_two, amount))

        # Create income transaction to the second account
        transaction = add_transaction(other_account, self.username, amount_converted, 'Income',
                                      f"Transfer from {self.account_id}")
        transaction.record_transaction()
        return True
