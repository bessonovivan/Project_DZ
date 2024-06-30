def get_mask_card_number(card_number):
    """Функция маскировки номера карты d ajhvfnt 7000 79** **** 6361"""
    str_card_number = str(card_number)
    return f"{str_card_number[:4]} {str_card_number[4:6]}** **** {str_card_number[-4:]}"


def get_mask_account(mask_account):
    """Функция маскировки номера счета в формате **4305"""
    str_mask_account = str(mask_account)
    return f"**{str_mask_account[-4:]}"
