import logging
import os

from config import LOGS_DIR

log_file_path = os.path.join(LOGS_DIR, "Application.log")
"""Логер для utils"""
utils_logger = logging.getLogger("utils")
utils_logger.setLevel(logging.DEBUG)

# Очищаем старые обработчики (если есть)
utils_logger.handlers.clear()

# Создаём обработчик для файла
file_handler = logging.FileHandler(log_file_path, mode="w", encoding="utf-8")
file_handler.setLevel(logging.DEBUG)

# Форматер
formatter = logging.Formatter("%(asctime)s %(filename)s %(levelname)s: %(message)s")
file_handler.setFormatter(formatter)

# Добавляем обработчик к логгеру
utils_logger.addHandler(file_handler)

"""Логер для masks"""
masks_logger = logging.getLogger("masks")
masks_logger.setLevel(logging.DEBUG)
masks_logger.handlers.clear()
file_handler = logging.FileHandler(log_file_path, mode="w", encoding="utf-8")
file_handler.setLevel(logging.DEBUG)
formatter = logging.Formatter("%(asctime)s %(filename)s %(levelname)s: %(message)s")
file_handler.setFormatter(formatter)
masks_logger.addHandler(file_handler)
