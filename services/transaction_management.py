# Transaction management module
from models.transaction import Transaction
from utils.file_handler import read_json
from utils.file_handler import write_json
from config.settings import Paths


# Addition a transaction
def add_transaction(account_id, amount, transaction_type, description):
    pass
    """data = {
        account.account_id: {
            "name": account.name,
            "currency": account.currency,
            "balance": account.balance
        }
    }
    path = Paths.path_accounts(login)
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
        return False"""


# get a list of account transactions in a given date range
def get_transactions(account_id, start_date, end_date):
    pass


def create_id_for_transaction(login):
    path = Paths.path_transactions(login)
    data_tmp = read_json(path)
    if not data_tmp:
        return 1
    else:
        id_transactions = len(data_tmp) + 1
        return id_transactions
