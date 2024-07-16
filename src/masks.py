def get_mask_card_number(card_number:str) -> str:
    """Функция маскировки номера карты d ajhvfnt 7000 79** **** 6361"""
    str_card_number = str(card_number)[-16:]
    return f"{str_card_number[:4]} {str_card_number[4:6]}** **** {str_card_number[-4:]}"


def get_mask_account(mask_account:str) -> str:
    """Функция маскировки номера счета в формате **4305"""
    str_mask_account = str(mask_account)
    return f"**{str_mask_account[-4:]}"

# Аргументом может быть строка типа
# Visa Platinum 7000792289606361
# , или
# Maestro 7000792289606361
# , или
# Счет 73654108430135874305