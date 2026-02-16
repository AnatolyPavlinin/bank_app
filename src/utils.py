import json
from typing import Any, Dict, List, Union

from config import PATH_JSON
from loggers import utils_logger
from src.external_api import get_converter


def get_list_dict_finance_transactions_json(full_path: str) -> List[Dict[str, Any]]:
    """Функция принимает на вход путь до JSON-файла и возвращает список словарей с данными
    о финансовых транзакциях. Если файл пустой, невалидный, содержит не список или не найден,
     функция возвращает пустой список."""
    utils_logger.info(f"Загружаем транзакции из файла: {full_path}")
    try:
        # Открываем файл и читаем данные
        with open(full_path, "r", encoding="utf-8") as f:
            utils_logger.info("Транзакции загружены успешно")
            return json.load(f)
    except (json.JSONDecodeError, FileNotFoundError) as e:
        # Если файл пустой или невалидный JSON
        utils_logger.error(f"Ошибка при загрузке файла: {e}")
        return []


def get_amount_transactions_in_rub(transaction: Dict[str, Any]) -> Union[float, str]:
    """Функция, принимает транзакцию и возвращает сумму транзакции (amount) в рублях, тип данных — float."""

    amount = transaction.get("operationAmount").get("amount")
    currency = transaction.get("operationAmount").get("currency").get("code")
    utils_logger.info(f"Конвертация транзакции: сумма {amount}, валюта: {currency}")

    if currency == "RUB":
        return amount
    elif currency in ["USD", "EUR"]:
        converter_result = get_converter(currency, amount)
        utils_logger.info(f"Конвертированная сумма: {converter_result}")
        return converter_result
    else:
        utils_logger.warning(f"Неизвестная валюта: {currency}")
        return "Неизвестная валюта"


# if __name__ == "__main__":
#     transactions = get_list_dict_finance_transactions_json(PATH_JSON)
#     print(get_amount_transactions_in_rub(transactions[8]))
#
#     transactions = get_list_dict_finance_transactions_json(PATH_JSON)
#     print(transactions)  # Выведет список транзакций или [] в случае ошибки
