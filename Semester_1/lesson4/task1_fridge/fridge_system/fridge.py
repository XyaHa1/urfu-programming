from decimal import Decimal
from typing import List, Dict

from .core import (
    CountItemsError,
    DateFormatError,
    SeparatorError,
    CharsTitleError,
    AmountError,
    Title,
    Amount,
    Date,
    Product,
    Validator,
)


class Fridge:
    def __init__(self, products: Dict):
        self._products = products

    def _add(self, product: Product):
        title = product.title.get()
        amount = product.amount.get()
        expiration_date = product.expiration_date.get()
        if title in self._products:
            self._products[title].append({"amount": amount, "expiration_date": expiration_date})
        else:
            self._products[title] = [{"amount": amount, "expiration_date": expiration_date}]


    def add_by_note(self, note):
        try:
            Validator.valid_separator(note)
            Validator.valid_count_items(note)
            items = note.split(",")

            Validator.valid_title(items[0])
            title = Title(items[0])

            Validator.valid_amount(items[1])
            amount = Amount(items[1])

            expiration_date = None
            if len(items) > 2 and items[2] != "":
                expiration_date = items[2].strip()
            Validator.valid_date(expiration_date)
            expiration_date = Date(expiration_date)

            product = Product(title, amount, expiration_date)
            self._add(product)
        except (
                CountItemsError,
                DateFormatError,
                SeparatorError,
                CharsTitleError,
                AmountError,
        ) as e:
            print(e)

    def find(self, words: str):
        words = words.split(", ")

        result = []
        for word in words:
            for title in self._products.keys():
                if word in title.lower():
                    result.append(title)

        return result

    def amount(self, words: str) -> List:
        titles = self.find(words)
        result = []
        for title in titles:
            current_amount = Decimal('0')
            for product in self._products[title]:
                current_amount += product["amount"]
            result.append((title, current_amount))

        return result
