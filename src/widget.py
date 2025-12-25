from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(inf_account_card: str) -> str:
    """Функция обрабатывает информацию о картах и о счетах"""
    if "счет" in inf_account_card.lower():
        number_card = inf_account_card[-20:]
        mask_card = get_mask_account(number_card)
        return f"Счет {mask_card}"
    else:
        number_card = inf_account_card[-16:]
        mask_card = get_mask_card_number(number_card)
        name_bank = inf_account_card[:-16]
        return f"{name_bank}{mask_card}"


def get_date(formatting_date: str) -> str:
    """Функция меняет формат даты"""
    correct_date = formatting_date[8:10] + "." + formatting_date[5:7] + "." + formatting_date[:4]
    return correct_date
