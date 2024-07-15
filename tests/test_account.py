import unittest
from models.account import Account
from config.settings import Paths
from pathlib import Path

user = User('Test', '1', 'test@email.com.')

class Test_User(unittest.TestCase):
    def test_register(self):
        Paths.users_json = Path("../data/users.json")
        result = user.register()
        self.assertEqual(result, False)

    def test_login(self):
        Paths.users_json = Path("../data/users.json")
        result = user.login()
        self.assertEqual(result, True)

    def test_update_profile(self):
        Paths.users_json = Path("../data/users.json")
        result = user.update_profile('1', 'user@user.com')
        self.assertEqual(result, True)


if __name__ == '__main__':
     unittest.main()
# тесты для класса Account