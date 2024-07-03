# from main import username
from utils import file_handler
from services import authentication
from config.settings import Paths
import os

from utils.file_handler import write_json, read_json


class Transaction:

    def __init__(self,  transaction_id, username,  account_id, amount, transaction_type, description, date):
        self.transaction_id = transaction_id
        self.username =username
        self.account_id = account_id
        self.amount = amount
        self.transaction_type = transaction_type
        self.description = description
        self.date = date
    # для записи транзакции в историю

    def record_transaction(self):
        pass
        data = {
            self.transaction_id: {
                "username":  self.username,
                "account_id": self.account_id,
                "amount": self.amount,
                "transaction_type": self.transaction_type,
                "description": self.description,
                "date": self.date
            }
        }
        path = Paths.path_transactions(self.username)
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
