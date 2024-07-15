# tests for the Account class

import unittest
from models.account import Account
from config.settings import Paths
from pathlib import Path

account = Account('1', 'mm', 'Luminor', 2, 1000, 0)
Paths.exchange_rates = Path("../data/exchange_rates.json")


class Test_Account(unittest.TestCase):
    def test_add_income(self):
        # Paths.users_json = Path("../data/users.json")
        result = account.add_income(100)
        self.assertEqual(result, 1000)

    def test_add_expense(self):
        # Paths.users_json = Path("../data/users.json")
        result = account.add_expense(100)
        self.assertEqual(result, 900)

    def test_get_balance(self):
        # Paths.users_json = Path("../data/users.json")
        result = account.get_balance()
        self.assertEqual(result, 1000)

    def test_delete_account(self):
        # Paths.users_json = Path("../data/users.json")
        result = account.delete_account()
        self.assertEqual(result, True)

    def test_transfer(self):
        # Paths.users_json = Path("../data/users.json")
        result = account.transfer('1', 2)
        self.assertEqual(result, True)


if __name__ == '__main__':
    unittest.main()

