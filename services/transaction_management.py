# Transaction management module

from datetime import datetime
import datetime
import json

from models.transaction import Transaction
# from models.account import Account
from utils.file_handler import read_json
from config.settings import Paths
from config.settings import Constants_and_variables
from functools import reduce


# Inner function for filter function
def filtering_fnc(data_tmp: dict):
    key, value = data_tmp
    if str(value['account_id']) != str(Constants_and_variables.account_id):  # First condition
        return False
    if str(value['transaction_type']) != str(
            Constants_and_variables.trans_type_account) and Constants_and_variables.trans_type_account:  # Second condition
        return False
    # Third condition between Date_start and Date_end
    if (datetime.datetime.strptime(value['date'], '%d.%m.%Y %H:%M:%S').date() < datetime.datetime.strptime(
            Constants_and_variables.date_start, '%d.%m.%Y').date()
            or datetime.datetime.strptime(value['date'], '%d.%m.%Y %H:%M:%S').date() > datetime.datetime.strptime(
                Constants_and_variables.date_end,
                '%d.%m.%Y').date()):
        return False

    return True


# Main function for filter
def generate_report_user_story_6(username, account_id, start_date, end_date, trans_type):
    accounts_tmp = read_json(Paths.path_accounts(username))
    try:
        account_name = accounts_tmp[str(account_id)]["name"]
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
            f"ID:{data}, account name: {account_name}, amount: {data_tmp_filtered[data]['amount']} {Constants_and_variables.currency[int(currency_name)]}, "
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
    return (total_income, total_expense)


def generate_report_user_story_7(username, account_id, start_date, end_date):
    total_income_list = []
    total_expense_list = []
    accounts_tmp = read_json(Paths.path_accounts(username))
    try:
        bank_name = accounts_tmp[str(account_id)]["name"]
    except:
        print("The account not exist!")
    currency_name = Constants_and_variables.currency[int(accounts_tmp[str(account_id)]["currency"])]
    Constants_and_variables.date_start = start_date
    Constants_and_variables.date_end = end_date
    Constants_and_variables.account_id = account_id
    path = Paths.path_transactions(username)
    data_tmp = json.loads(path.read_text(encoding='utf-8'))
    data_tmp_filtered = dict(filter(filtering_fnc, data_tmp.items()))
    for key, value in data_tmp_filtered.items():
        if str(value['transaction_type']) == 'Income':
            total_income_list.append(value['amount'])
        else:
            total_expense_list.append(value['amount'])

    # Calling reduce function
    if total_income_list:
        total_income = reduce(lambda x, y: x + y, total_income_list)
    else:
        total_income = 0
    if total_expense_list:
        total_expense = reduce(lambda x, y: x + y, total_expense_list)
    else:
        total_expense = 0

    report = (
        f"Общий доход: {total_income} {currency_name}\n"
        f"Общий расход: {total_expense} {currency_name}\n"
        f"Конечный баланс: {total_income - total_expense} {currency_name}\n"
    )
    print(report)


# Addition a transaction
def add_transaction(account_id, username, amount, transaction_type, description):
    transaction = Transaction(create_id_for_transaction(username), username, account_id, amount, transaction_type,
                              description, datetime.datetime.now().strftime('%d.%m.%Y %H:%M:%S'))
    return transaction


def create_id_for_transaction(login):
    path = Paths.path_transactions(login)
    data_tmp = read_json(path)
    if not data_tmp:
        return 1
    else:
        id_transactions = len(data_tmp) + 1
        return id_transactions
