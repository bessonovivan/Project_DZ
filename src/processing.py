import datetime

from typing import Union
from typing import Dict, List


def filter_by_state(last_dict: List[Dict], value_key: str = "EXECUTED") -> List[Dict]:
    """Принимает список словарей и ключ: state (по умолчанию 'EXECUTED').
    Возвращает новый список словарей, содержащий словари соответствующих ключ"""
    new_list_dict = []
    for i in range(len(last_dict)):
        if last_dict[i].get("state") == value_key:
            new_list_dict.append(last_dict[i])
    return new_list_dict


def sort_by_date(list_of_dictionary: Union[list, dict], sort_sequence: bool = True) -> Union[list, dict]:
    """Функция, сортирующая список словарей по дате"""
    list_with_date = list()
    for my_dictionary in list_of_dictionary:
        if "date" in my_dictionary.keys():
            list_with_date.append(my_dictionary)
    sorted_of_date_list = sorted(
        list_with_date,
        key=lambda x: datetime.datetime.strptime(x.get("date"), "%Y-%m-%dT%H:%M:%S.%f"),
        reverse=sort_sequence,
    )
    return sorted_of_date_list