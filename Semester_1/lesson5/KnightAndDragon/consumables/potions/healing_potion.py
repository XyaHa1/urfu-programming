from ..potions import Potion


class HealingPotion(Potion):
    def __init__(self, name: str, max_count: int, healing_amount: int):
        super().__init__(name, max_count, healing_amount)
