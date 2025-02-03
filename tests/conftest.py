import pytest


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