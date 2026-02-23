import re
from collections import Counter


def process_bank_search(data: list[dict], search: str) -> list[dict]:
    """Фильтрует список словарей с данными о банковских операциях, оставляя только те,
    в описании которых встречается заданная строка."""
    try:
        result = []
        for operation in data:
            if "description" in operation and re.search(search, operation["description"], re.IGNORECASE):
                result.append(operation)
        return result
    except re.error:
        return []


def process_bank_operations(data: list[dict], categories: list) -> dict:
    """Считает количество операций в каждой категории."""
    counter = Counter()
    for operation in data:
        description = operation.get("description", "").lower()
        for category in categories:
            if category.lower() in description:
                counter[category] += 1
    return dict(counter)


# if __name__ == '__main__':
#     operations = [
#         {"amount": 500, "description": "Оплата кафе"},
#         {"amount": 1000, "description": "Перевод другу"},
#         {"amount": 300, "description": "Покупка в МАГАЗИНЕ"},
#     ]
#     found = process_bank_search(operations, "перевод")
#     print(found)

#    Пример использования:
#     data = [
#         {'id': 1, 'amount': 1000, 'description': 'food'},
#         {'id': 2, 'amount': 500, 'description': 'transport'},
#         {'id': 3, 'amount': 2000, 'description': 'entertainment'},
#         {'id': 4, 'amount': 300, 'description': 'food'},
#         {'id': 5, 'amount': 3000, 'description': 'entertainment'}
#     ]
#     categories = ['food', 'transport', 'entertainment']
#     result = process_bank_operations(data, categories)
#     print(result)
