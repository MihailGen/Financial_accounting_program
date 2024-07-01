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
