from dataclasses import dataclass
from datetime import date, datetime
from decimal import Decimal

from ._config import DATE_FORMAT


class Title:
    def __init__(self, title: str):
        self._title: str = self.__to_format(title)

    def __str__(self) -> str:
        return self.title

    @property
    def title(self):
        return self._title

    def __to_format(self, title):
        return " ".join(
            item.capitalize()
            for item in " ".join(title.strip().lower().split(" "))
            .replace(" - ", "-")
            .split(" ")
        )


class Amount:
    def __init__(self, amount: str):
        self._amount: Decimal = Decimal(amount)

    def __str__(self) -> Decimal:
        return self._amount

    @property
    def amount(self):
        return self._amount


class Date:
    def __init__(self, date: str | None):
        if date is not None:
            self._date: date = datetime.strptime(date, DATE_FORMAT).date()
        else:
            self._date = None

    def __str__(self) -> date | None:
        return self._date

    @property
    def date(self):
        return self._date


@dataclass
class Product:
    title: Title
    amount: Amount
    expiration_date: Date
