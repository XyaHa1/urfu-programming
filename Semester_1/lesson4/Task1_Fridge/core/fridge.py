from datetime import date, datetime
from dataclasses import dataclass
from decimal import Decimal
from typing import Dict,Union


goods = {
    'Пельмени Универсальные': [
        # Первая партия продукта 'Пельмени Универсальные':
        {'amount': Decimal('0.5'), 'expiration_date': date(2023, 7, 15)},
        # Вторая партия продукта 'Пельмени Универсальные':
        {'amount': Decimal('2'), 'expiration_date': date(2023, 8, 1)},
    ],
    'Вода': [
        {'amount': Decimal('1.5'), 'expiration_date': None}
    ],
}

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

