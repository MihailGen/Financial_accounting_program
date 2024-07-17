from functools import wraps
# from utils.currency_converter import currency
from utils.file_handler import read_json
from config.settings import Paths, Constants_and_variables
from utils.file_handler import write_json
import os
import datetime


def logger_for_Transaction(type_operation):
    def logger(func):
        @wraps(func)
        def wrapper(self):
            result = func(self)
            path = Paths.logs_json

            if type_operation == "Write transaction to history":
                data = {
                    self.date: f"| {type_operation} | {self.username} | {self.transaction_type}: {self.description}, {self.amount}, ID Account:{self.account_id}"
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


def logger_for_Account(type_operation_account):
    def logger(func):
        @wraps(func)
        def wrapper(self, *args, **kwargs):
            result = func(self, *args, **kwargs)
            path = Paths.logs_json

            if type_operation_account == "Get balance":
                data = {
                    datetime.datetime.now().strftime(
                        '%d.%m.%Y %H:%M:%S'): f"| {type_operation_account} | {self.username} | Account ID: {self.account_id} Balance: {self.balance} {Constants_and_variables.currency[self.currency]}"
                }

            if type_operation_account == "Delete account":
                data = {
                    datetime.datetime.now().strftime(
                        '%d.%m.%Y %H:%M:%S'): f"| {type_operation_account} | {self.username} | Account ID: {self.account_id}"
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
                        '%d.%m.%y %H:%M:%S'): f"| {type_operation} | {args[0]} | Account name: {args[2]}, Currency: {args[3]} {Constants_and_variables.currency[int(args[2])]}\n"
                }

            if type_operation == "Update account":
                data = {
                    current_date.strftime(
                        '%d.%m.%y %H:%M:%S'): f"| {type_operation} | {args[0]} | Account ID: {args[1]}, Currency: {Constants_and_variables.currency[args[3]]}, Balance: {args[4]}\n"
                }

            elif type_operation == "Registration":
                data = {
                    current_date.strftime('%d.%m.%y %H:%M:%S'): f"| {type_operation} | {args[0]} | Success: {result}\n"
                }

            elif type_operation == "Update user information":
                data = {
                    current_date.strftime(
                        '%d.%m.%y %H:%M:%S'): f"| {type_operation} | Password: IT IS SECRET , email: {args[2]} | Success: {result}\n"
                }


            elif type_operation == "Login to system":
                data = {
                    current_date.strftime(
                        '%d.%m.%y %H:%M:%S'): f"| {type_operation} | Login: {args[0]}, Password: {args[1]} | Success: {result}!!!\n"
                }
            elif type_operation == "Logout":
                data = {
                    current_date.strftime(
                        '%d.%m.%y %H:%M:%S'): f"| {type_operation} | Login: {args[0]} | Success!!!\n"
                }

            elif type_operation == "Currency converter":
                data = {
                    current_date.strftime(
                        '%d.%m.%y %H:%M:%S'): f"| {type_operation} | Login: {args[0]} | From currency: {args[0]} To currency: {args[1]} Amount: {args[2]} \n"
                }

            elif type_operation == "Report user story 6":
                data = {
                    current_date.strftime(
                        '%d.%m.%y %H:%M:%S'): f"| {type_operation} | Login: {args[0]} | Account ID: {args[1]} Date start: {args[2]} Date end: {args[3]} Transaction Type: {args[4]} \n"
                }

            elif type_operation == "Report user story 7":
                data = {
                    current_date.strftime(
                        '%d.%m.%y %H:%M:%S'): f"| {type_operation} | Login: {args[0]} | Account ID: {args[1]} Date start: {args[2]} Date end: {args[3]} \n"
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
