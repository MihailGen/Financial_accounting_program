import datetime
from config.settings import Paths
from utils.file_handler import write_json
from utils.file_handler import read_json
import os
import asyncio
import aiohttp

from utils.logger import logger_events

currency = ("Reserved", "rub", "usd", "eur", "kzt", "cny", "byn")

@logger_events("Currency converter")
async def converter(currency_first, currency_two, amount: float):
    date_today = datetime.datetime.now().strftime('%d.%m.%y')
    data = read_json(Paths.exchange_rates)
    if not data or date_today not in data:
        print("converter from internet")
        result = await converter_from_internet(currency_first, currency_two, amount)
        await list_currency_rates_to_file(Paths.service_path)
        return result
    else:
        if data[date_today]:
            print("converter from cash")
            result = converter_from_cash(currency_first, currency_two, amount)
        return result


async def converter_from_internet(currency_first, currency_two, amount=1):
    content = await get_content(Paths.service_path)
    if currency_first == "usd" or currency_two == "USD":
        rate_currency_to = content[currency_two]["rate"]
        result = round(amount * rate_currency_to, 2)
    elif currency_two == "usd" or currency_two == "USD":
        rate_currency = content[currency_first]["rate"]
        result = round(amount / rate_currency, 2)
    else:
        rate_currency = content[currency_first]["rate"]
        rate_currency_to = content[currency_two]["rate"]
        result = round((amount / rate_currency) * rate_currency_to, 2)
    return result


def converter_from_cash(currency_first, currency_two, amount=1):
    date = datetime.datetime.now().strftime('%d.%m.%y')
    data = read_json(Paths.exchange_rates)
    if currency_first == currency_two:
        return amount
    if currency_first == "usd" or currency_two == "USD":
        rate_currency_to = data[date][currency_two]["rate"]
        result = round(amount * rate_currency_to, 2)
    elif currency_two == "usd" or currency_two == "USD":
        rate_currency = data[date][currency_first]["rate"]
        result = round(amount / rate_currency, 2)
    else:
        rate_currency = data[date][currency_first]["rate"]
        rate_currency_to = data[date][currency_two]["rate"]
        result = round((amount / rate_currency) * rate_currency_to, 2)
    return result


async def list_currency_rates_to_file(path_to_service):
    path_to_file = Paths.exchange_rates
    content = await get_content(path_to_service)
    print(content)
    data = {
        datetime.datetime.now().strftime('%d.%m.%y'): content
    }
    try:
        if not os.path.isfile(path_to_file) or os.stat(path_to_file).st_size == 0:
            with open(path_to_file, "w", encoding="utf-8") as file:
                write_json(path_to_file, data)
        else:
            data_tmp = read_json(path_to_file)
            data_tmp.update(data)
            if data_tmp:
                write_json(path_to_file, data_tmp)
            else:
                write_json(path_to_file, data)
        return True
    except FileNotFoundError:
        return False


async def get_content(path_to_service):
    async with aiohttp.ClientSession() as session:
        async with session.get(path_to_service) as response:
            data = await response.json()
    return data


async def get_currency_list(path_to_service):
    content = await get_content(path_to_service)
    if not content:
        print("internet")
        content = await get_content(path_to_service)
    for name in content:
        print(f"{name}: {content[name]['name']}")