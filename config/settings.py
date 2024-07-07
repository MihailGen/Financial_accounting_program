import json
from ast import parse
from pathlib import Path
from dataclasses import dataclass

import requests


@dataclass
class Paths:
    users_json = Path("data/users.json")
    accounts_json =  Path("data/accounts")
    transactions_json = Path("data/transactions")
    logs_json = Path("data/logs/logs.json")

    @classmethod
    def path_accounts(self, login):
        str_for_path = "data/accounts/" + login + "_accounts.json"
        return Path(str_for_path)

    @classmethod
    def path_transactions(self, login):
        str_for_path = "data/transactions/" + login + "_transactions.json"
        return Path(str_for_path)


CONST_FOR_HASH = 68429
currency = ("Reserved", "rub", "usd", "eur", "kzt", "uan", "cny", "byn")
api_path = "https://currate.ru/api/?get=rates&pairs=USDRUB,EURRUB&key=fb69fb257939f616ac7ab878fbdeac4c"

def get_exchange_list(currency, currency_to, amount=1):
    content = json.loads(requests.get(f"https://www.floatrates.com/daily/{currency}.json").content)
    content = content[currency_to]["rate"]
    print(content)
    result = round(content * amount, 2)
    print(result)
    return result

get_exchange_list("rub", "cny", amount=100)