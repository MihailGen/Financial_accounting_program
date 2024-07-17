import os
import json
import time
from pathlib import Path
from config.settings import Paths
import config.settings


def read_json(path):
    try:
        if (os.stat(path).st_size == 0):
            return False
    except FileNotFoundError:
        print("FileNotFoundError")
        return False
    try:
        return json.loads(path.read_text(encoding='utf-8'))
    except json.decoder.JSONDecodeError:
        print("Invalid JSON")


def write_json(path, data):
    try:
        return path.write_text(json.dumps(data), encoding='utf-8')
    except json.decoder.JSONDecodeError:
        print("Invalid JSON")


def update_account_balance(username, account_id, balance):
    path = Paths.path_accounts(username)
    # for tests
    try:
        if (os.stat(path).st_size == 0):
            path = Path("../data/accounts/mm_accounts.json")
    except FileNotFoundError as e:
        path = Path("../data/accounts/mm_accounts.json")
    data_tmp = read_json(path)
    # data_tmp = read_json(Path("../data/accounts/mm_accounts.json"))
    data_tmp[account_id]["balance"] = balance
    write_json(path, data_tmp)

def update_account_status(username, account_id, status):
    path = Paths.path_accounts(username)
    try:
        if (os.stat(path).st_size == 0):
            path = Path("../data/accounts/mm_accounts.json")
    except FileNotFoundError as e:
        path = Path("../data/accounts/mm_accounts.json")
    data_tmp = read_json(path)
    data_tmp[account_id]['status'] = status
    if write_json(path, data_tmp):
        return True
    else:
        return False
