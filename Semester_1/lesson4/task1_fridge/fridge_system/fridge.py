from Semester_1.lesson4.task1_fridge.fridge_system.core.exceptions import *
from Semester_1.lesson4.task1_fridge.fridge_system.core.models import *
from Semester_1.lesson4.task1_fridge.fridge_system.core.validators import Validator


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


class Fridge:
    def __init__(self, goods=None):
        if goods is None:
            goods = dict()
        self._goods = goods

    def _add(self, product: Product):
        title = product.title.get()
        amount = product.amount.get()
        expiration_date = product.expiration_date.get()

        if title in self._goods:
            self._goods[title].append(
                {"amount": amount, "expiration_date": expiration_date}
            )
        else:
            self._goods[title] = [
                {"amount": amount, "expiration_date": expiration_date}
            ]

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
                InvalidSeparator,
                InvalidCharsTitle,
        ) as e:
            print(e)
