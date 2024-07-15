# тесты для сервисов


import unittest
from models.account import Account
from config.settings import Paths
from pathlib import Path

account = Account('1', 'mm', 'Luminor', 2, 1000, 0)
Paths.exchange_rates = Path("../data/exchange_rates.json")


class Test_Services(unittest.TestCase):
    def test_add_income(self):
        # Paths.users_json = Path("../data/users.json")
        result = account.add_income(100)
        self.assertEqual(result, 1000)



if __name__ == '__main__':
    unittest.main()
