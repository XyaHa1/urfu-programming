from datetime import date
from decimal import Decimal

import pytest

from core import (
    Validator,
    DateFormatError,
    AmountError,
    CountItemsError,
    InvalidSeparator,
    InvalidCharsTitle,
    Fridge,
)


class TestValidator:

    @pytest.mark.parametrize("valid", [" 0.5", "1.5", "  2.5", "00.00"])
    def test_valid_amount(self, valid):
        Validator.valid_amount(valid)

    @pytest.mark.parametrize(
        "invalid", [" .5 ", "  1,5", "-2,5", "13.50.2", "  50.  ", "-1.2"]
    )
    def test_invalid_amount(self, invalid):
        with pytest.raises(AmountError):
            Validator.valid_amount(invalid)

    @pytest.mark.parametrize("valid", ["2023-07-11", "2023-12-01", "2025-03-01"])
    def test_valid_date(self, valid):
        Validator.valid_date(valid)

    @pytest.mark.parametrize(
        "invalid",
        [
            "2023-01 01 ",
            "2023-01-01 12:00",
            "2023 01",
            "09 01 2024",
            "28-02-2024",
            "28-2026-04",
            "2024 02-29",
            "19.05.24",
        ],
    )
    def test_invalid_date(self, invalid):
        with pytest.raises(DateFormatError):
            Validator.valid_date(invalid)

    @pytest.mark.parametrize(
        "valid",
        [
            "pepsi ,  0.5,  ",
            "coca-cola, 1.5, 2023-07-11",
            "sprite  ,2.5, 2023-12-01",
            "coffee, 0.05",
            "carrot   2, 2023-07-11 ",
        ],
    )
    def test_valid_count_items(self, valid):
        Validator.valid_count_items(valid)

    @pytest.mark.parametrize(
        "invalid", ["coca-cola , 1.5 , 2023-07-11, 2023-07-11", "cheeps   0.5   ", "  "]
    )
    def test_invalid_count_items(self, invalid):
        with pytest.raises(CountItemsError):
            Validator.valid_count_items(invalid)

    @pytest.mark.parametrize(
        "valid", ["coca-cola , 1.5 , 2023-07-11", "pepsi ,  0.5,  ", "coffee, 0.05"]
    )
    def test_valid_separator(self, valid):
        Validator.valid_separator(valid)

    @pytest.mark.parametrize(
        "invalid",
        [
            "coca-cola; 1.5; 2023-07-11, 2023-07-11",
            "  carrot; 2.5, 2023-07-11",
            "potato \ 2.5 2023-07-11",
            "  carrot, 2.5 ~ 2023-07-11",
        ],
    )
    def test_invalid_separator(self, invalid):
        with pytest.raises(InvalidSeparator):
            Validator.valid_separator(invalid)

    @pytest.mark.parametrize(
        "valid",
        [
            "пельмени",
            "Картофель",
            "milk",
            "coca -cola",
            "coca-cola",
            "пельмени Уральские",
        ],
    )
    def test_valid_title(self, valid):
        Validator.valid_title(valid)

    @pytest.mark.parametrize("invalid", ["Кофе1н", "1арковь", "картофеля.нет"])
    def test_invalid_title(self, invalid):
        with pytest.raises(InvalidCharsTitle):
            Validator.valid_title(invalid)


class TestFridge:

    def test_add_case_1(self):
        f = Fridge({})
        f.add_by_note("Пельмени    , 100  ,")
        assert f._goods == {
            "Пельмени": [{"amount": Decimal("100"), "expiration_date": None}]
        }

    def test_add_case_2(self):
        f = Fridge({})
        f.add_by_note("Пельмени    , 100       , 2023-01-26")
        assert f._goods == {
            "Пельмени": [
                {"amount": Decimal("100"), "expiration_date": date(2023, 1, 26)}
            ]
        }

    def test_add_case_3(self):
        f = Fridge({})
        f.add_by_note("Пельмени , 100 , 2023-01-26")
        f.add_by_note("Сок  , 1.5 , 2024-12-26")
        assert f._goods == {
            "Пельмени": [
                {"amount": Decimal("100"), "expiration_date": date(2023, 1, 26)}
            ],
            "Сок": [{"amount": Decimal("1.5"), "expiration_date": date(2024, 12, 26)}],
        }

    def test_add_case_4(self):
        f = Fridge({})
        f.add_by_note("Кофе   , 0.7")
        assert f._goods == {
            "Кофе": [{"amount": Decimal("0.7"), "expiration_date": None}]
        }

    def test_add_case_5(self):
        f = Fridge({})
        f.add_by_note("Пепси, 0.97, 2025-10-13")
        assert f._goods == {
            "Пепси": [
                {"amount": Decimal("0.97"), "expiration_date": date(2025, 10, 13)}
            ]
        }

    def test_add_case_6(self):
        f = Fridge({})
        f.add_by_note("Картофель, 1, 2100-10-13")
        assert f._goods == {
            "Картофель": [
                {"amount": Decimal("1"), "expiration_date": date(2100, 10, 13)}
            ]
        }
