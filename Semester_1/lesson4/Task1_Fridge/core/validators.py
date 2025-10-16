from datetime import datetime
from decimal import Decimal, InvalidOperation

from ._config import DATE_FORMAT
from .exceptions import (
    DateFormatError,
    CountItemsError,
    AmountError,
    InvalidSeparator,
    InvalidCharsTitle,
)


class Validator:

    @staticmethod
    def valid_title(title: str):
        letters = {chr(i) for i in range(ord("a"), ord("z") + 1)}
        letters.update({chr(i) for i in range(ord("а"), ord("я") + 1)})
        letters.update({"-", " ", "ё"})

        for char in title.strip().lower():
            if char not in letters:
                raise InvalidCharsTitle()

    @staticmethod
    def valid_amount(amount: str):
        amount = amount.strip()
        if amount.count(".") > 1:
            raise AmountError()

        if amount.count(",") > 0:
            raise AmountError()

        if len(amount.split(".")) > 2:
            raise AmountError()

        if amount.startswith(".") or amount.endswith("."):
            raise AmountError()

        try:
            d = Decimal(amount)
        except InvalidOperation:
            raise AmountError()

        if d < 0:
            raise AmountError()

    @staticmethod
    def valid_date(date_str: str | None):
        if date_str is None:
            return
        try:
            datetime.strptime(date_str, DATE_FORMAT)
        except ValueError:
            raise DateFormatError()

    @staticmethod
    def valid_separator(s: str):
        invalid_separators = [";", "|", "/", "\\", ":", "~"]
        if any(sep in s for sep in invalid_separators):
            raise InvalidSeparator()

    @staticmethod
    def valid_count_items(items: str):
        if len(items.strip()) == 0:
            raise CountItemsError()

        items = [item.strip() for item in items.split(",")]
        items = [item for item in items if len(item) > 0]

        if len(items) < 2 or len(items) > 3:
            raise CountItemsError()

        if len(items[0]) == 0 or len(items[1]) == 0:
            raise CountItemsError()
