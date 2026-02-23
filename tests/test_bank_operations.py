from src.bank_operations import process_bank_operations, process_bank_search

test_data = [
    {"id": 1, "amount": 1000, "description": "food"},
    {"id": 2, "amount": 500, "description": "transport"},
    {"id": 3, "amount": 2000, "description": "entertainment"},
    {"id": 4, "amount": 300, "description": "food"},
    {"id": 5, "amount": 3000, "description": "entertainment"},
]


# Тесты для функции process_bank_search
def test_process_bank_search_try() -> None:
    result = process_bank_search(test_data, "food")
    assert len(result) == 2
    assert all("food" in operat["description"].lower() for operat in result)


def test_process_bank_search_no_matches() -> None:
    result = process_bank_search(test_data, "прием")
    assert len(result) == 0


def test_process_bank_search_invalid() -> None:
    result = process_bank_search(test_data, "пр[ием")
    assert result == []


# Тест для функции process_bank_operations
def test_process_bank_operations() -> None:
    categories = ["food", "transport", "entertainment"]
    result = process_bank_operations(test_data, categories)
    assert result == {"food": 2, "transport": 1, "entertainment": 2}
