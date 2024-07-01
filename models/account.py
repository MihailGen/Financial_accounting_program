from utils import file_handler
from services import authentication


class Account:
    def __init__(self,  account_id,  name, currency, balance, status):
        self.account_id = account_id
        self.name = name
        self.currency = currency
        self.balance = balance
        self.status = status

    # Добавление дохода
    def add_income(self, amount):
        self.balance += amount

    # Регистрация расхода
    def add_expense(self, amount):
        if amount > self.balance:
            self.balance -= amount
        else:
            print('Insufficient funds')

    # Получение текущего баланса
    def get_balance(self):
        return self.balance

    # Осуществление перевода средств на другой счет
    def transfer(self, other_account, amount):
        pass
