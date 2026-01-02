from src.masks import get_mask_card_number
from src.masks import get_mask_account
from src.processing import filter_by_state
from src.processing import sort_by_date

card_number = "1111222233334444"
masked_number = get_mask_card_number(card_number)
print(masked_number)

account_number = 123456789987456123
masked_acc_number = get_mask_account(account_number)
print(masked_acc_number)


if __name__ == "__main__":
    list_of_dictionaries = [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]
    print(filter_by_state(list_of_dictionaries))

    print(sort_by_date(list_of_dictionaries))