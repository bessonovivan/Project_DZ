import pytest

from src.widget import get_date, mask_account_card


def test_mask_account_card(new_card: str):
    assert mask_account_card(new_card) == "Visa Platinum 7000 79** **** 6361"


def test_get_data(old_data: str):
    assert get_date(old_data) == "11.03.2024"