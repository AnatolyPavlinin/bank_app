from unittest.mock import mock_open, patch

from src.utils import get_amount_transactions_in_rub, get_list_dict_finance_transactions_json


def test_get_list_dict_finance_transactions() -> None:
    with patch("builtins.open", mock_open(read_data='{"1": "2"}')):
        assert get_list_dict_finance_transactions_json("") == {"1": "2"}

    with patch("builtins.open", mock_open(read_data='{"1": "2"')):
        assert get_list_dict_finance_transactions_json("") == []


def test_get_amount_transactions_in_rub() -> None:
    with patch("requests.get") as r_mock:
        r_mock.return_value.json.return_value = {"result": 123}
        assert (
            get_amount_transactions_in_rub({"operationAmount": {"amount": "79114.93", "currency": {"code": "USD"}}})
            == 123
        )

    assert (
        get_amount_transactions_in_rub({"operationAmount": {"amount": "34114.93", "currency": {"code": "RUB"}}})
        == "34114.93"
    )

    assert (
        get_amount_transactions_in_rub({"operationAmount": {"amount": "34114.93", "currency": {"code": "GBR"}}})
        == "Неизвестная валюта"
    )
