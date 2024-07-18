from utils.logger import logger_for_Transaction
from config.settings import Paths
from pathlib import Path
import os
import inspect

from utils.file_handler import write_json, read_json


class Transaction:

    def __init__(self, transaction_id: int, username: str, account_id: int, amount: float, transaction_type: str,
                 description: str, date: str):
        self.transaction_id = transaction_id
        self.username = username
        self.account_id = account_id
        self.amount = amount
        self.transaction_type = transaction_type
        self.description = description
        self.date = date

    # для записи транзакции в историю
    @logger_for_Transaction("Write transaction to history")
    def record_transaction(self):
        # Change the balance in account
        path = Paths.path_accounts(self.username)
        # For tests
        try:
            if (os.stat(path).st_size == 0):
                path = Path("../data/accounts/mm_accounts.json")
        except FileNotFoundError:
            path = Path("../data/accounts/mm_accounts.json")
        data_tmp = read_json(path)
        if self.transaction_type == "Income":
            data_tmp[self.account_id]["balance"] = float(data_tmp[self.account_id]["balance"] - self.amount)
        else:
            if data_tmp[self.account_id]["balance"] >= self.amount:
                data_tmp[self.account_id]["balance"] = float(data_tmp[self.account_id]["balance"] - self.amount)
            else:
                print('You don`t have enough funds in your account!\nTransaction canceled!\n')
                return False

        write_json(path, data_tmp)

        # Write transaction to file
        data = {
            self.transaction_id: {
                "username": self.username,
                "account_id": self.account_id,
                "amount": self.amount,
                "transaction_type": self.transaction_type,
                "description": self.description,
                "date": self.date
            }
        }

        path = Paths.path_transactions(self.username)

        # for test only
        try:
            if inspect.stack()[2][3] == '_callTestMethod':
                path = Path("../data/transactions/mm_transactions.json")

        except FileNotFoundError as e:
            path = Paths.path_transactions(self.username)

        # если файла не существует, записываем в него данные сразу
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

        return True
