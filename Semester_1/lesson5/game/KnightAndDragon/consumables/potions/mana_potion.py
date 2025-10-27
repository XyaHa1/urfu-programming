from ..potions.potion import Potion


class ManaPotion(Potion):
    def __init__(self, name: str, max_count: int, mana_amount: int):
        super().__init__(name, max_count, mana_amount)
