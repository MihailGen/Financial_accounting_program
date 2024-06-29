from pathlib import Path
from dataclasses import dataclass


@dataclass
class Paths:
    users_json = Path("data/users.json")
    accounts_json = Path("data/accounts/")
    def path_accounts(self, login):
        str_for_path = str(self.accounts_json) + f"/{login}_accounts.json"
        print(str_for_path)
        return Path(str_for_path)




CONST_FOR_HASH = 68429

