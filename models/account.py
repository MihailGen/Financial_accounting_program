from utils import file_handler
from services import authentication


class Account:

    def __init__(self,  account_id,  name, currency, balance):
        self.account_id = account_id
        self.name = name
        self.currency = currency
        self.balance = balance

    # Добавление дохода
    def add_income(self, amount):
        pass

    # Регистрация расхода
    def add_expense(self, amount):
        pass

    # Получение текущего баланса
    def get_balance(self):
        pass

    # Осуществление перевода средств на другой счет
    def transfer(self, other_account, amount):
        pass
