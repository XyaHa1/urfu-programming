import pytest
from core import Validator, DateFormatError, AmountError, CountItemsError

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
            assert Validator().valid_count_items('100 Сок')
            assert Validator().valid_count_items('193 Сок 2023-01-26')


if __name__ == '__main__':
    TestValidator().start()

