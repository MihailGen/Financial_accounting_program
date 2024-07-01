from pathlib import Path
from dataclasses import dataclass



@dataclass
class Paths:
    users_json = Path("data/users.json")
    accounts_json = Path("data/accounts")
    @classmethod
    def path_accounts(self, login):
        str_for_path = "data/accounts/" + login + "_accounts.json"
        print(str_for_path + "----from file_handler")
        return Path(str_for_path)
        # return str_for_path

CONST_FOR_HASH = 68429

