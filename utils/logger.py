from functools import wraps
from config.settings import Paths
from utils.file_handler import read_json
from utils.file_handler import write_json
import os


def logger_transact(type_operation):
    def logger(func):
        @wraps(func)
        def wrapper(self):
            result = func(self)
            # log_sting = "%s | %s | %s | %s" % (self.date, self.type_operation, self.username, self.description)
            path = Paths.logs_json
            data = {
                self.date: [" | " + self.transaction_type + " | ", type_operation + " | ", self.username + " | ",
                            self.transaction_type + ":" + self.description + " " +
                            str(self.amount) + "RUB" + " Account: "
                            + self.account_id + " | "]
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


def logger_events(type_operation):
    def logger(func):
        @wraps(func)
        def wrapper(self):
            result = func(self)
            # log_sting = "%s | %s | %s | %s" % (self.date, self.type_operation, self.username, self.description)
            path = Paths.logs_json
            data = {
                self.date: [" | " + self.transaction_type + " | ", type_operation + " | ", self.username + " | ",
                            self.transaction_type + ":" + self.description + " " +
                            str(self.amount) + "RUB" + " Account: "
                            + self.account_id + " | "]
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
