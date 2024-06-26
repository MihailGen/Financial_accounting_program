import json
import time
from pathlib import Path


# Запись нового пользователя в файл всех пользователей
def user_to_datafile (data):
    path = Path("data/data_file.json")
    data_tmp = json.loads(path.read_text(encoding='utf-8'))
    data_tmp.update(data)
    path.write_text(json.dumps(data_tmp), encoding='utf-8')

# проверка пароля
def login(username, password):
    path = Path("data/data_file.json")
    data_tmp = json.loads(path.read_text(encoding='utf-8'))
    if "username" in data_tmp:
        
