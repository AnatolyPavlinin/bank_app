from typing import Iterable


def filter_by_state(list_of_dictionaries: Iterable[dict], state: str = "EXECUTED") -> Iterable:
    """Функция, которая принимает список словарей и опционально значение для ключа state
    (по умолчанию 'EXECUTED'). Функция возвращает новый список словарей, содержащий только те
    словари, у которых ключ state соответствует указанному значению."""
    filtered_list = []
    state_upper = state.upper()  # Приводим к верхнему регистру

    for dictionary in list_of_dictionaries:
        if "state" in dictionary:
            state_value = dictionary["state"]
            if isinstance(state_value, str) and state_value.upper() == state_upper:
                filtered_list.append(dictionary)
    return filtered_list


def sort_by_date(list_of_dictionaries: Iterable[dict], decreasing: bool = True) -> Iterable:
    """Функция, которая принимает список словарей и необязательный параметр,
    задающий порядок сортировки (по умолчанию — убывание). Функция возвращает
     новый список, отсортированный по дате (date)."""
    sorted_list_by_data = sorted(
        list_of_dictionaries,
        key=lambda list_of_dic: int(list_of_dic["date"].split("T")[0].replace("-", "")),
        reverse=decreasing,
    )
    return sorted_list_by_data
