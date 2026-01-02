from typing import Iterable


def filter_by_state(list_of_dictionaries: list, state: str = "EXECUTED") -> Iterable:
    """Функция, которая принимает список словарей и опционально значение для ключа state
    (по умолчанию 'EXECUTED'). Функция возвращает новый список словарей, содержащий только те
    словари, у которых ключ state соответствует указанному значению."""
    filtered_list = []
    state_upper = state.upper()   # Приводим к верхнему регистру

    for dictionary in list_of_dictionaries:
        if "state" in dictionary:
            state_value = dictionary["state"]
            if isinstance(state_value, str) and state_value.upper() == state_upper:
                filtered_list.append(dictionary)
    return filtered_list