# тесты для сервисов

import asyncio
import unittest
from models.account import Account
from services import account_management, authentication
from pathlib import Path
from config.settings import Paths
from utils import currency_converter
from unittest import IsolatedAsyncioTestCase

account = Account('5', 'mm', 'Luminor', 2, 1000, 0)
Paths.exchange_rates = Path("../data/exchange_rates.json")


class Test(IsolatedAsyncioTestCase):
    async def test_converter_from_internet(self):
        result = await currency_converter.converter_from_internet('rub', 'usd', 100)
        self.assertEqual(result, 1.13)

    async def test_converter_from_cash(self):
        result = await currency_converter.converter_from_cash('rub', 'usd', 100)
        self.assertEqual(result, 1.13)

    async def converter(self):
        Paths.exchange_rates = Path("../data/exchange_rates.json")
        result = await currency_converter.converter('rub', 'usd', 100)
        self.assertEqual(result, 1.13)



class Test_Services(unittest.TestCase):
    def test_isValid(self):
        result = account_management.isValid("user&inbox.ru")
        self.assertEqual(result, False)

    def test_save_account_to_json(self):
        result = account_management.save_account_to_json('mm', account)
        self.assertEqual(result, True)

    def test_create_account(self):
        result = account_management.create_account('mm', 'TestAccount', 2, 10)
        self.assertEqual(result.balance, 10)

    def test_create_account_object_from_json(self):
        result = account_management.create_account_object_from_json('mm', '4')
        self.assertEqual(result.name, 'Swedbanka')

    def test_check_if_account_exists(self):
        result = account_management.check_if_account_exists('4', 'mm')
        self.assertEqual(result, True)

    def create_id_for_account(self):
        result = account_management.create_id_for_account('mm')
        self.assertEqual(result, 5)

    def test_login_fnc(self):
        Paths.users_json = Path("../data/users.json")
        result = authentication.login_fnc('mm', 'm')
        self.assertEqual(result, True)

    def test_register(self):
        Paths.users_json = Path("../data/users.json")
        result = authentication.register('mmm', 'm', 'mmm@email.ru')
        self.assertEqual(result, False)

    def test_user_mail_from_Json(self):
        Paths.users_json = Path("../data/users.json")
        result = authentication.user_mail_from_Json('mm')
        self.assertEqual(result, "vronskij_new@mail.ru")

    def test_hash_funct(self):
        result = authentication.hash_funct('1')
        self.assertEqual(result, '4949')


if __name__ == '__main__':
    unittest.main()
