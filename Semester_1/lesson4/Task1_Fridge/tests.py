import pytest
from core import Validator, DateFormatError, AmountError, CountItemsError
from core import Fridge
from decimal import Decimal
from datetime import date


class TestValidator:

    def start(self):
        self._test_amount()
        self._test_date()
        self._test_count_items()

    def _test_amount(self):
        assert Validator().valid_amount('100') == True
        assert Validator().valid_amount('0.00') == True
        assert Validator().valid_amount('00.00') == True

        with pytest.raises(AmountError):
            assert Validator().valid_amount('-150,00')
            assert Validator().valid_amount('150,00')
            assert Validator().valid_amount(' ')
            assert Validator().valid_amount('-1,0')

    def _test_date(self):
        assert Validator().valid_date('2021-01-01') == True

        with pytest.raises(DateFormatError):
            assert Validator().valid_date('2026-01-01')
            assert Validator().valid_date('2021-01-01')
            assert Validator().valid_date('2021-13-12')
            assert Validator().valid_date('2021 13-12')
            assert Validator().valid_date('2021 13 12')

    def _test_count_items(self):
        assert Validator().valid_count_items('100, 100') == True
        assert Validator().valid_count_items('100, 100, 100') == True

        with pytest.raises(CountItemsError):
            assert Validator().valid_count_items('100, ')
            assert Validator().valid_count_items('100, 100, 100, 100')
            assert Validator().valid_count_items(' ')
            assert Validator().valid_count_items('Сок 100')
            assert Validator().valid_count_items('Сок 193 2023-01-26')


class TestFridge:

    def start(self):
        self._test_fridge_add()

    def _test_fridge_add(self):
        def case_1():
            f = Fridge({})
            f.add_by_note('Пельмени, 100,')
            assert f._goods == {'Пельмени': [{'amount': Decimal('100'), 'expiration_date': None}]}
        case_1()

        def case_2():
            f = Fridge({})
            f.add_by_note('Пельмени, 100, 2023-01-26')
            assert f._goods == {'Пельмени': [{'amount': Decimal('100'), 'expiration_date': date(2023, 1, 26)}]}
        case_2()

        def case_3():
            f = Fridge({})
            f.add_by_note('Пельмени, 100, 2023-01-26')
            f.add_by_note('Сок, 1.5, 2024-12-26')
            assert f._goods == {'Пельмени': [{'amount': Decimal('100'), 'expiration_date': date(2023, 1, 26)}],
                                'Сок': [{'amount': Decimal('1.5'), 'expiration_date': date(2024, 12, 26)}]}
        case_3()

        def case_4():
            f = Fridge({})
            f.add_by_note('Кофе, 0.7')
            assert f._goods == {'Кофе': [{'amount': Decimal('0.7'), 'expiration_date': None}]}
        case_4()


if __name__ == '__main__':
    TestValidator().start()
    TestFridge().start()

