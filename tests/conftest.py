import pytest

from typing import List, Union, Dict


@pytest.fixture
def standart_numbers_for_get_masks_card() -> str:
    return "7000 55** **** 6059"


@pytest.fixture
def not_standart_numbers_for_get_masks_card() -> str:
    return "Неправильно задан номер карты  16 цифр"


@pytest.fixture
def standart_numbers_for_get_masks_card_account():
    return '**4305'

@pytest.fixture
def not_standart_numbers_for_get_masks_card_account() -> str:
    return "проверьте номер счета, он должен быть 20 цифр"

@pytest.fixture
def to_mask_card() -> str:
    return "73654108430135874305"


@pytest.fixture
def to_mask() -> str:
    return "7000792289606361"


@pytest.fixture
def expected() -> str:
    return "8675874657756475"


@pytest.fixture
def new_card() -> str:
    return "Visa 7000 79** **** 6361"


@pytest.fixture
def old_data() -> str:
    return "2024-03-11T02:26:18.671407"

@pytest.fixture
def last_dict() -> List[Dict[str, Union[str, float, int]]]:
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]