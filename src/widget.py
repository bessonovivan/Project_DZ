from masks import get_mask_card_number
from masks import get_mask_account


def mask_account_card(input_str: str) -> str | None:
    """Функция  которая умеет обрабатывать информацию как о картах, так и о счетах"""
    if ('Visa' in input_str) or ('Maestro' in input_str):
        return f"{input_str[:-17]} {get_mask_card_number(input_str)}"
    elif 'Счет' in input_str:
        return f"Счет {get_mask_account(input_str)}"
    else:
        return None


def get_date(inf_data: str) -> str:
    """ Преобразование даты """
    data_split = inf_data.split('T')[0]
    return f"{data_split.split('-')[-1]}.{data_split.split('-')[-2]}.{data_split.split('-')[-3]}"


def src():
    return None