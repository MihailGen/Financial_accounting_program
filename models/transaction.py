from utils import file_handler
from services import authentication


class Transaction:

    def __init__(self,  transaction_id,  account_id, amount, transaction_type, date):
        self.transaction_id = transaction_id
        self.account_ide = account_id
        self.amount = amount
        self.transaction_type = transaction_type
        self.date = date

    # для записи транзакции в историю
    def record_transaction(self):
        pass
