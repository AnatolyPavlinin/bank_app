from unittest.mock import patch

from src.external_api import get_converter


def test_get_converter_usd() -> None:
    with patch("requests.get") as r_mock:
        r_mock.return_value.json.return_value = {"result": 75.50}

        assert get_converter("USD", "1") == 75.50


def test_get_converter_eur() -> None:
    with patch("requests.get") as r_mock:
        r_mock.return_value.json.return_value = {"result": 80.25}

        assert get_converter("EUR", "1") == 80.25
