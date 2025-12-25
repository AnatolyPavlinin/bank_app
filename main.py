from src.masks import get_mask_card_number
from src.masks import get_mask_account

card_number = "1111222233334444"
masked_number = get_mask_card_number(card_number)
print(masked_number)

account_number = 123456789987456123
masked_acc_number = get_mask_account(account_number)
print(masked_acc_number)
