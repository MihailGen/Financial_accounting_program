from pathlib import Path
from dataclasses import dataclass
import aiohttp


@dataclass
class Paths:
    users_json = Path("data/users.json")
    accounts_json = Path("data/accounts")
    transactions_json = Path("data/transactions")
    logs_json = Path("data/logs/logs.json")
    exchange_rates = Path("data/exchange_rates.json")
    service_path = "https://www.floatrates.com/daily/usd.json"
    date_start = ''
    date_end = ''
    account_id =''

    @classmethod
    def path_accounts(self, login):
        str_for_path = "data/accounts/" + login + "_accounts.json"
        return Path(str_for_path)

    @classmethod
    def path_transactions(self, login):
        str_for_path = "data/transactions/" + login + "_transactions.json"
        return Path(str_for_path)

@dataclass
class Constants_and_variables:
    trans_type = ('Income', 'Payment')
    trans_type_account = ''
    date_start = ''
    date_end = ''
    account_id = ''
    currency = ("Reserved", "rub", "usd", "eur", "kzt", "cny", "byn")




CONST_FOR_HASH = 68429
