from pathlib import Path
from dataclasses import dataclass



@dataclass
class Paths:
    users_json = Path("data/users.json")
    accounts_json =  Path("data/accounts")
    transactions_json = Path("data/transactions")
    @classmethod
    def path_accounts(self, login):
        str_for_path = "data/accounts/" + login + "_accounts.json"
        return Path(str_for_path)

    @classmethod
    def path_transactions(self, login):
        str_for_path = "data/transactions/" + login + "_transactions.json"
        return Path(str_for_path)


CONST_FOR_HASH = 68429

