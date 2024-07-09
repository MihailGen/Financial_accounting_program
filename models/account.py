from utils.file_handler import read_json
from utils.file_handler import write_json
from config.settings import Paths
# from services.account_management import update_account_balance


class Account:
    def __init__(self,  account_id, username, name, currency, balance, status=0):
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


    # Регистрация расхода
    def add_expense(self, amount):
        if float(amount) < self.balance:
            self.balance -= amount
            update_account_balance(self.username, self.account_id, self.balance)
        else:
            print('Insufficient funds')

    # Получение текущего баланса
    def get_balance(self):
        return self.balance

    # Осуществление перевода средств на другой счет
    def transfer(self, other_account, amount):
        pass

def update_account_balance(username, account_id, balance):
    print(f"update_account_balance{username, account_id, balance}")
    # print('Start update_account_balance')
    path = Paths.path_accounts(username)
    # print(path)
    data_tmp = read_json(path)
    # print(data_tmp)
    data_tmp[account_id]["balance"] = balance
    write_json(path, data_tmp)