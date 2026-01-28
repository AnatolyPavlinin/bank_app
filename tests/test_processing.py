from typing import Union

import pytest

from src.processing import filter_by_state, sort_by_date


@pytest.mark.parametrize(
    "state, expected",
    [
        ("EXECUTED", [41428829, 594226727]),
        ("CANCELED", [939719570]),
        ("PENDING", [615064591]),
        ("UNKNOWN", []),
    ],
)
def test_filter_by_state(card_operations: Union[list], state: str, expected: list) -> None:
    result = filter_by_state(card_operations, state)
    assert [t["id"] for t in result] == expected


@pytest.mark.parametrize(
    "reverse, expected",
    [
        (True, 41428829),
        (False, 939719570),
    ],
)
def test_sort_by_date(card_operations: Union[str], reverse: bool, expected: str) -> None:
    assert sort_by_date(
        [
            {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
            {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
            {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
            {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        ]
    ) == [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ]
