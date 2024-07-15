from utils.logger import logger_for_classmethod
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
    @logger_for_classmethod("Write transaction to history")
    def record_transaction(self):
        if inspect.currentframe().f_back.f_code.co_name == '_callTestMethod':
            # print(f"Вызывающая: {inspect.currentframe().f_back.f_code.co_name}")
            print('!!!Super')
        # Change the balance in account
        path = Paths.path_accounts(self.username)

        # For tests
        try:
            if (os.stat(path).st_size == 0):
                path = Path("../data/accounts/mm_accounts.json")
        except FileNotFoundError as e:
            path = Path("../data/accounts/mm_accounts.json")

        data_tmp = read_json(path)
        if self.transaction_type == "Income":
            data_tmp[self.account_id]["balance"] == round((float(data_tmp[self.account_id]["balance"]) + self.amount),
                                                          2)
        else:
            data_tmp[self.account_id]["balance"] == round((float(data_tmp[self.account_id]["balance"]) - self.amount),
                                                          2)
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

        try:
            if (os.stat(path).st_size == 0):
                path = Path("../data/transactions/mm_transactions.json")
        except FileNotFoundError as e:
            path = Path("../data/transactions/mm_transactions.json")

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
