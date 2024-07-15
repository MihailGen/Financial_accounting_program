# тесты для класса Transaction
import unittest
from models.transaction import Transaction
from services.transaction_management import create_id_for_transaction
from config.settings import Paths
from pathlib import Path
import datetime
import inspect


transaction = Transaction('46', 'mm', '1', 2, 'Paiment', 'Na korm kotu', "05.07.2024 13:22:21")
Paths.exchange_rates = Path("../data/exchange_rates.json")


class Test_Transaction(unittest.TestCase):
    def test_record_transaction(self):
        result = transaction.record_transaction
        self.assertEqual(result, True)

if __name__ == '__main__':
    unittest.main()

