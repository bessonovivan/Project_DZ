from src.masks import get_mask_card_number, get_mask_account


def test_get_mask_card_number(standart_numbers_for_get_masks_card):
    assert get_mask_card_number('7000552289606059') == standart_numbers_for_get_masks_card


def test_get_mask_card_number_wrong(not_standart_numbers_for_get_masks_card):
    assert get_mask_card_number('700079228009000606361') == not_standart_numbers_for_get_masks_card
    assert get_mask_card_number('70006361') == not_standart_numbers_for_get_masks_card
    assert get_mask_card_number('700079228900') == not_standart_numbers_for_get_masks_card


def test_get_mask_account():
    assert get_mask_account('73654108430135874305') == '**4305'
    assert get_mask_account('73654108430135876005') == '**6005'
