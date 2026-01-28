import pytest


@pytest.fixture
def card_number() -> list[str]:
    return [
        "7000792289606361",
        "1111222233334444",
        "5555666677778888",
        "1234 5678 1234 5678",
    ]


@pytest.fixture
def account_number() -> list[str]:
    return [
        "73654108430135874305",
        "98765432198765432198",
        "1234",
    ]


@pytest.fixture
def inform_card() -> list[str]:
    return [
        "Maestro 1596837868705199",
        "MasterCard 7158300734726758",
        "Visa Classic 6831982476737658",
        "Visa Platinum 8990922113665229",
        "Visa Gold 5999414228426353",
    ]


@pytest.fixture
def inform_account() -> list[str]:
    return [
        "Счет 64686473678894779589",
        "Счет 35383033474447895560",
        "Счет 73654108430135874305",
    ]


@pytest.fixture
def formatting_date() -> list[str]:
    return [
        "2024-03-11T02:26:18.671407",
        "2024-09-21T02:26:18.671407",
        "2024-01-01T02:26:18.671407",
        "2024-10-16T02:26:18.671407",
    ]


@pytest.fixture
def card_operations() -> list[dict]:
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "CANCELED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "EXECUTED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "PENDING", "date": "2018-10-14T08:21:33.419441"},
    ]
