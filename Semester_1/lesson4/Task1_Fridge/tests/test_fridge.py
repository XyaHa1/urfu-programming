from datetime import date
from decimal import Decimal

from ..core import Fridge


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
        f.add_by_note("Пепси,  0.97   , 2025-10-13")
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

    def test_add_case_7(self):
        f = Fridge({})
        f.add_by_note("pepsi - cola, 1, 2100-10-13")
        assert f._goods == {
            "Pepsi-cola": [
                {"amount": Decimal("1"), "expiration_date": date(2100, 10, 13)}
            ]
        }

    def test_add_case_8(self):
        f = Fridge({})
        f.add_by_note(" пеЛЬмени цеЗарь, 1, 2100-10-13")
        assert f._goods == {
            "Пельмени Цезарь": [
                {"amount": Decimal("1"), "expiration_date": date(2100, 10, 13)}
            ]
        }

    def test_add_case_9(self):
        f = Fridge({})
        f.add_by_note("pepsi - cola vanilla, 1, 2100-10-13")
        assert f._goods == {
            "Pepsi-cola Vanilla": [
                {"amount": Decimal("1"), "expiration_date": date(2100, 10, 13)}
            ]
        }
