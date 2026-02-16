from mypy.types import Union

from loggers import masks_logger


def get_mask_card_number(card_number: Union[str]) -> str:
    """Функция принимает на вход номер карты и возвращает ее маску"""
    card_number = str(card_number)
    if len(card_number) != 16:
        masks_logger.error("Неправильный формат номера карты")
        raise ValueError("Номер карты должен содержать ровно 16 цифр.")

    masked_card_number = f"{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"
    masks_logger.info(f"Маскировка банковской карты: {masked_card_number}")

    return masked_card_number


def get_mask_account(account_number: Union[str]) -> str:
    """Функция принимает на вход номер счета и возвращает его маску"""
    account_number = str(account_number)
    last_four_digits = account_number[-4:]
    masks_logger.info(f"Маскировка банковского счета: {last_four_digits}")

    return f"**{last_four_digits}"


# if __name__ == "__main__":
#      # print(get_mask_card_number("7000792289606361"))
#      # print(get_mask_card_number("7000 7922 8960 6361"))
#      # print(get_mask_card_number("7000 7922 8960 661"))
#      # print(get_mask_account("73654108430135874305"))
