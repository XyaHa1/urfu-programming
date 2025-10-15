from datetime import datetime
from .exceptions import DateFormatError, CountItemsError, AmountError, InvalidSeparator
from ._config import DATE_FORMAT
from decimal import Decimal, InvalidOperation


class Validator:

    @staticmethod
    def valid_amount(amount: str):
        amount = amount.strip()
        if amount.count('.') > 1:
            raise AmountError()

        if amount.count(',') > 0:
            raise AmountError()

        if len(amount.split('.')) > 2:
            raise AmountError()

        if amount.startswith('.') or amount.endswith('.'):
            raise AmountError()

        try:
            d = Decimal(amount)
        except InvalidOperation:
            raise AmountError()

        if d < 0:
            raise AmountError()

    @staticmethod
    def valid_date(date_str: str | None):
        try:
            datetime.strptime(date_str, DATE_FORMAT)
        except ValueError:
            raise DateFormatError()

    @staticmethod
    def valid_separator(s: str):
        invalid_separators = [';', '|', '/', '\\', ':', '~']
        if any(sep in s for sep in invalid_separators):
            raise InvalidSeparator()


    @staticmethod
    def valid_count_items(items: str):
        if len(items.strip()) == 0:
            raise CountItemsError()

        items = [item.strip() for item in items.split(',')]
        items = [item for item in items if len(item) > 0]


        if len(items) < 2 or len(items) > 3:
            raise CountItemsError()

        if len(items[0]) == 0 or len(items[1]) == 0:
            raise CountItemsError()
