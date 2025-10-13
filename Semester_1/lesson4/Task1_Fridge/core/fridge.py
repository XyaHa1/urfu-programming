from datetime import date, datetime
from dataclasses import dataclass
from decimal import Decimal
from typing import Dict, Union
from .exceptions import *
from .validators import Validator
from ._config import DATE_FORMAT


# goods = {
#     'Пельмени Универсальные': [
#         # Первая партия продукта 'Пельмени Универсальные':
#         {'amount': Decimal('0.5'), 'expiration_date': date(2023, 7, 15)},
#         # Вторая партия продукта 'Пельмени Универсальные':
#         {'amount': Decimal('2'), 'expiration_date': date(2023, 8, 1)},
#     ],
#     'Вода': [
#         {'amount': Decimal('1.5'), 'expiration_date': None}
#     ],
# }

expiration_date_type = Union[None, date]

@dataclass
class Product:
    name: str
    amount: Decimal
    expiration_date: expiration_date_type


class Fridge:
    def __init__(self, goods: Dict = dict()):
        self._goods = goods


    def _add(self, product: Product):
        name = product.name
        amount = product.amount
        expiration_date = product.expiration_date
        if name in self._goods:
            self._goods[name].append({'amount': amount, 'expiration_date': expiration_date})
        else:
            self._goods[name] = [{'amount': amount, 'expiration_date': expiration_date}]

    def add_by_note(self, note):
        try:
            Validator.valid_count_items(note.strip())
            items = note.split(',')

            title = items[0].strip()

            amount = items[1].strip()
            Validator.valid_amount(amount)
            amount = Decimal(amount)

            expiration_date = None
            if len(items) > 2 and items[2] != '':
                expiration_date = items[2].strip()
                Validator.valid_date(expiration_date)
                expiration_date = datetime.strptime(expiration_date, DATE_FORMAT).date()

            product = Product(title, amount, expiration_date)
            self._add(product)
        except (CountItemsError, DateFormatError) as e:
            print(e)
