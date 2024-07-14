from functools import wraps
from config.settings import Paths
from utils.currency_converter import currency
from utils.file_handler import read_json
from utils.file_handler import write_json
import os
import datetime


def logger_for_classmethod(type_operation):
    def logger(func):
        @wraps(func)
        def wrapper(self):
            result = func(self)
            path = Paths.logs_json
            data = {
                self.date: f"| {type_operation} | {self.username} | {self.transaction_type}: {self.description}, {self.amount} {currency[0]}., ID Account:{self.account_id}"
            }
            try:

                # If there is no file, write immediately
                if not os.path.isfile(path):
                    with open(path, "w", encoding="utf-8") as file:
                        write_json(path, data)

                # Otherwise, pull out the structure from the file, supplement it and write it down again
                else:
                    data_tmp = read_json(path)
                    data_tmp.update(data)
                    write_json(path, data_tmp)
            except FileNotFoundError:
                print("File logs error")
            return result

        return wrapper

    return logger


def logger_events(type_operation) -> object:
    def logger(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            current_date = datetime.datetime.now()
            path = Paths.logs_json
            if type_operation == "Create account":
                data = {
                    current_date.strftime(
                        '%d.%m.%y %H:%M:%S'): f"| {type_operation} | {args[0]} | Account name: {args[1]}, Start balance: {args[3]} {currency[int(args[2])]}\n"
                }
            elif type_operation == "Registration":
                data = {
                    current_date.strftime('%d.%m.%y %H:%M:%S'): f"| {type_operation} | {args[0]} | Success: {result}\n"
                }
            elif type_operation == "Login to system":
                data = {
                    current_date.strftime('%d.%m.%y %H:%M:%S'): f"| {type_operation} | Login: {args[0]}, Password: {args[1]} | Success: {result}!!!\n"
                }
            elif type_operation == "Logout":
                data = {
                    current_date.strftime(
                        '%d.%m.%y %H:%M:%S'): f"| {type_operation} | Login: {args[0]} | Success!!!\n"
                }

            else:
                data = {
                    current_date.strftime('%d.%m.%y %H:%M:%S'): f"Error"
                }

            try:
                # If there is no file, write immediately
                if not os.path.isfile(path):
                    with open(path, "w", encoding="utf-8") as file:
                        write_json(path, data)

                # Otherwise, pull out the structure from the file, supplement it and write it down again
                else:
                    data_tmp = read_json(path)
                    data_tmp.update(data)
                    write_json(path, data_tmp)
            except FileNotFoundError:
                print("File logs error")
            return result
        return wrapper
    return logger


def create_id_for_logs():
    path = Paths.logs_json
    data_tmp = read_json(path)
    if not data_tmp:
        return 1
    else:
        id_transactions = len(data_tmp) + 1
        return id_transactions
