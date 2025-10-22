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

    def add(self, potion_name: str, count: int = 1) -> None:
        potion = self._potions.get(potion_name)
        added = potion.add(count)
        if added > 0:
            print(
                f"*({self._potions[potion_name]}) Отлично, теперь у меня {self._potions[potion_name].current_count} из {self._potions[potion_name].max_count}*")
            return
        print(f"*({self._potions[potion_name]}) Не могу положить, нет места*")
