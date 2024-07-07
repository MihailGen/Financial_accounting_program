import json
from idlelib.iomenu import encoding

import requests
import datetime
from config.settings import Paths
from utils.file_handler import write_json
from utils.file_handler import read_json
import os

currency = ("Reserved", "rub", "usd", "eur", "kzt", "uan", "cny", "byn")
api_path = "https://www.floatrates.com/daily/usd.json"


def converter(currenc, currency_to, amount=1):
    date_today = datetime.datetime.now().strftime('%d.%m.%y')
    print(date_today)
    try:
        data = read_json(Paths.exchange_rates)
        if not data:
            data = list_carrencyrates_to_file(api_path)
    except:
        list_carrencyrates_to_file(api_path)
    print(data)
    if date_today in data:
        print("converter_from_cash")
        converter_from_cash(currenc, currency_to, amount=1)
    else:
        print("converter_from_internet")
        converter_from_internet(currenc, currency_to, amount=1)
        list_carrencyrates_to_file(api_path)


def converter_from_internet(currency, currency_to, amount=1):
    content = json.loads(requests.get(api_path).content)
    if currency == "usd" or currency_to == "USD":
        rate_currency_to = content[currency_to]["rate"]
        result = round(amount * rate_currency_to, 2)
    elif currency_to == "usd" or currency_to == "USD":
        rate_currency = content[currency]["rate"]
        result = round(amount / rate_currency, 2)
    else:
        rate_currency = content[currency]["rate"]
        rate_currency_to = content[currency_to]["rate"]
        result = round((amount / rate_currency) * rate_currency_to, 2)
    print(result)
    return result


def converter_from_cash(currenc, currency_to, amount=1):
    date = datetime.datetime.now().strftime('%d.%m.%y')
    data = read_json(Paths.exchange_rates)
    if currenc == "usd" or currency == "USD":
        rate_currency_to = data[date][currency_to]["rate"]
        result = round(amount * rate_currency_to, 2)
    elif currency_to == "usd" or currency_to == "USD":
        rate_currency = data[date][currenc]["rate"]
        result = round(amount / rate_currency, 2)
    else:
        rate_currency = data[date][currenc]["rate"]
        rate_currency_to = data[date][currency_to]["rate"]
        result = round((amount / rate_currency) * rate_currency_to, 2)
    print(result)
    return result


async def list_carrencyrates_to_file(path_to_internet):
    path_to_file = Paths.exchange_rates
    content = json.loads(requests.get(path_to_internet).content)
    data = {
        datetime.datetime.now().strftime('%d.%m.%y'): content
    }
    try:
        if not os.path.isfile(path_to_file):
            with open(Paths.exchange_rates, "w", encoding="utf-8") as file:
                write_json(path_to_file, data)
            # иначе - вытаскиваем из файла структуру, дополняем её и вновь записываем
        else:
            data_tmp = read_json(path_to_file)
            data_tmp.update(data)
            if data_tmp:
                write_json(path_to_file, data_tmp)
            else:
                write_json(path_to_file, data)
        return content
    except FileNotFoundError:
        return False

# converter("rub", "eur", amount=100000)