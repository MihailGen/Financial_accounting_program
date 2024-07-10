# Transaction management module
from utils.logger import logger_for_classmethod
from config.settings import Paths
import os
from utils.file_handler import write_json, read_json
from datetime import datetime
import datetime
import json
from models.transaction import Transaction
from utils.file_handler import read_json
from utils.file_handler import write_json
from config.settings import Paths
from config.settings import Constants_and_variables


def filtering_fnc(data_tmp: dict):
    key, value = data_tmp
    if str(value['account_id']) != str(Constants_and_variables.account_id):  # first condition
        return False

    if str(value['transaction_type']) != str(Constants_and_variables.trans_type_account):  # second condition
        return False

    if value['date'][0:10] < (datetime.datetime.strptime(Constants_and_variables.date_start, '%d.%m.%Y')).strftime(
            '%d.%m.%Y') or value['date'][0:10] > (
            datetime.datetime.strptime(Constants_and_variables.date_end, '%d.%m.%Y')).strftime(
        '%d.%m.%Y'):  # third condition
        return False

    return True


def generate_report(username, account_id, start_date, end_date, trans_type):
    accounts_tmp = read_json(Paths.path_accounts(username))
    bank_name = accounts_tmp[str(account_id)]["name"]
    currency_name = accounts_tmp[str(account_id)]["currency"]
    print(bank_name, currency_name)
    Constants_and_variables.date_start = start_date
    Constants_and_variables.date_end = end_date
    Constants_and_variables.account_id = account_id
    Constants_and_variables.trans_type_account = trans_type
    path = Paths.path_transactions(username)
    data_tmp = json.loads(path.read_text(encoding='utf-8'))
    data_tmp_filtered = dict(filter(filtering_fnc, data_tmp.items()))
    for data in data_tmp_filtered:
        print(
            f"ID:{data}, account name: {bank_name}, amount: {data_tmp_filtered[data]['amount']}{Constants_and_variables.currency[int(currency_name)]}, "
            f"type: {data_tmp_filtered[data]['transaction_type']}, description: {data_tmp_filtered[data]['description']}, "
            f"{data_tmp_filtered[data]['date']}")
    # return data_tmp_filtered


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
    print(path)
    data_tmp = read_json(path)
    if not data_tmp:
        return 1
    else:
        id_transactions = len(data_tmp) + 1
        return id_transactions

# generate_report(1, 1, 4)
# generate_report(1, datetime.datetime.strptime('01.07.2024', '%d.%m.%Y') , datetime.datetime.strptime('08.07.2024', '%d.%m.%Y'))
