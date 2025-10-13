from datetime import datetime
from .exceptions import DateFormatError, CountItemsError, AmountError
from ._config import DATE_FORMAT


class Validator:

    @staticmethod
    def valid_amount(amount: str):
        if amount.count('.') > 1:
            raise AmountError()

        if amount.count(',') > 0:
            raise AmountError()

        for ch in amount:
            if not ch.isdigit():
                if ch != '.':
                    raise AmountError()

        return True


    @staticmethod
    def valid_date(date_str: str | None):
        if date_str is None:
            return

        try:
            datetime.strptime(date_str, DATE_FORMAT)
            return True
        except ValueError:
            raise DateFormatError()

    @staticmethod
    def valid_count_items(items: str):
        if len(items) == 0:
            raise CountItemsError()

        items = items.split(',')
        if len(items) < 2:
            raise CountItemsError()

        return True
