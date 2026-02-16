import os

ROOT_DIR = os.path.dirname(__file__)  # корневой каталог
DATA_DIR = os.path.join(ROOT_DIR, "data")
LOGS_DIR = os.path.join(ROOT_DIR, "logs")

PATH_JSON = os.path.join(DATA_DIR, "operations.json")  # путь json