from typing import Dict

from .potion import Potion


class PotionManager:
    def __init__(self, potions: Dict[str, Potion]):
        self._potions = potions

    def use(self, potion_name) -> int:
        potion = self._potions.get(potion_name)
        if potion.can_use():
            print(f"*Использую {potion}: +{potion.value}*")
            return potion.use()
        print(f"*({potion}) Закончилось, не могу им пользоваться*")
        return 0
