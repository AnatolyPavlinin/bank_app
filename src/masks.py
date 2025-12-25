def get_mask_card_number(card_number: str) -> str:
    """Функция принимает на вход номер карты и возвращает ее маску"""
    card_number = str(card_number)
    if len(card_number) != 16:
        raise ValueError("Номер карты должен содержать ровно 16 цифр.")

    masked_card_number = f"{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"

    return masked_card_number


def get_mask_account(account_number: str) -> str:
    """Функция принимает на вход номер счета и возвращает его маску"""
    account_number = str(account_number)
    last_four_digits = account_number[-4:]

    return f"**{last_four_digits}"



