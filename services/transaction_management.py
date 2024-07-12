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
from functools import reduce


# Inner function for filter function
def filtering_fnc(data_tmp: dict):
    key, value = data_tmp
    if str(value['account_id']) != str(Constants_and_variables.account_id):  # first condition
        return False

    # if not Constants_and_variables.trans_type_account:
    #     return True
    if str(value['transaction_type']) != str(Constants_and_variables.trans_type_account) and Constants_and_variables.trans_type_account:  # second condition
        return False

    if value['date'][0:10] < (datetime.datetime.strptime(Constants_and_variables.date_start, '%d.%m.%Y')).strftime(
            '%d.%m.%Y') or value['date'][0:10] > (
            datetime.datetime.strptime(Constants_and_variables.date_end, '%d.%m.%Y')).strftime(
        '%d.%m.%Y'):  # third condition
        return False

    return True


# Main function for filter
def generate_report_user_story_6(username, account_id, start_date, end_date, trans_type):
    accounts_tmp = read_json(Paths.path_accounts(username))
    try:
        bank_name = accounts_tmp[str(account_id)]["name"]
    except:
        print("The account not exist!")
    currency_name = accounts_tmp[str(account_id)]["currency"]
    Constants_and_variables.date_start = start_date
    Constants_and_variables.date_end = end_date
    Constants_and_variables.account_id = account_id
    Constants_and_variables.trans_type_account = trans_type
    path = Paths.path_transactions(username)
    data_tmp = json.loads(path.read_text(encoding='utf-8'))
    # Calling function for filter function
    data_tmp_filtered = dict(filter(filtering_fnc, data_tmp.items()))
    # Printing filtered transactions list
    for data in data_tmp_filtered:
        print(
            f"ID:{data}, account name: {bank_name}, amount: {data_tmp_filtered[data]['amount']}{Constants_and_variables.currency[int(currency_name)]}, "
            f"type: {data_tmp_filtered[data]['transaction_type']}, description: {data_tmp_filtered[data]['description']}, "
            f"{data_tmp_filtered[data]['date']}")


# Inner function for reduce function
def reduce_fnc(data_tmp: dict):
    total_income = 0
    total_expense = 0
    key, value = data_tmp

    if str(value['account_id']) != str(Constants_and_variables.account_id):  # first condition
        return False

    if value['date'][0:10] < (datetime.datetime.strptime(Constants_and_variables.date_start, '%d.%m.%Y')).strftime(
            '%d.%m.%Y') or value['date'][0:10] > (
            datetime.datetime.strptime(Constants_and_variables.date_end, '%d.%m.%Y')).strftime(
        '%d.%m.%Y'):  # third condition
        return False

    if str(value['transaction_type']) == "Income":  # second condition
        total_income += float(value['amount'])
    if str(value['transaction_type']) == "Payment":  # second condition
        total_expense += float(value['amount'])

    print(total_income + " " + total_expense)

    return (total_income, total_expense)


def generate_report_user_story_7(username, account_id, start_date, end_date):
    total_list = []
    total_income_list = []
    total_expense_list = []
    accounts_tmp = read_json(Paths.path_accounts(username))
    try:
        bank_name = accounts_tmp[str(account_id)]["name"]
    except:
        print("The account not exist!")
    currency_name = accounts_tmp[str(account_id)]["currency"]
    Constants_and_variables.date_start = start_date
    Constants_and_variables.date_end = end_date
    Constants_and_variables.account_id = account_id
    Constants_and_variables.trans_type_account = 'Income'
    path = Paths.path_transactions(username)
    data_tmp = json.loads(path.read_text(encoding='utf-8'))
    print("!")
    print(data_tmp)

    data_tmp_Income = dict(filter(filtering_fnc, data_tmp.items()))
    Constants_and_variables.trans_type_account = 'Payment'
    data_tmp_Payment = dict(filter(filtering_fnc, data_tmp.items()))
    print("!!!")
    print(data_tmp_Payment)
    for key, value in data_tmp_Payment.items():
        if str(value['transaction_type']) == 'Income':
            # total_list.append(value['amount'])
            total_income_list.append(value['amount'])
        else:
            total_expense_list.append(value['amount'] * -1)

    total_list = total_income_list + total_expense_list

    # Calling function for reduce function
    # total_income_list = reduce(lambda a, b: a+b, data_tmp.items())
    total_report = reduce(lambda x, y: x + y, total_list)
    print('total_report', total_report)

    # Printing filtered transactions list
    # for data in data_tmp_filtered:
    #     print(
    #         f"ID:{data}, account name: {bank_name}, amount: {data_tmp_filtered[data]['amount']}{Constants_and_variables.currency[int(currency_name)]}, "
    #         f"type: {data_tmp_filtered[data]['transaction_type']}, description: {data_tmp_filtered[data]['description']}, "
    #         f"{data_tmp_filtered[data]['date']}")


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
