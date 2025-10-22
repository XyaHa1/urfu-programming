from abc import ABC


class Potion(ABC):
    def __init__(self, name: str, max_count: int, solute: int):
        self._name: str = name
        self._max_count: int = max_count
        self._current_count: int = max_count
        self._solute: int = solute

    def __str__(self):
        return f"{self._name} ({self._current_count}/{self._max_count})"

    def add(self, count=1) -> None:
        if self._current_count < self._max_count:
            self._current_count = min(self._current_count + count, self._max_count)

    def use(self) -> int:
        self._current_count -= 1
        return self._solute

    def can_use(self) -> bool:
        return self._current_count > 0


class HealingPotion(Potion):
    def __init__(self, name, max_count, healing):
        super().__init__(name, max_count, healing)


class ManaPotion(Potion):
    def __init__(self, name, max_count, mana):
        super().__init__(name, max_count, mana)


class PotionManager:
    def __init__(self, *potions):
        self._potions = dict(potions)

    def use(self, potion_name) -> int:
        if self._potions[potion_name].can_use():
            return self._potions[potion_name].use()

    def add(self, potion_name, count=1) -> None:
        self._potions[potion_name].add(count)

    def can_use(self, potion_name) -> bool:
        return self._potions[potion_name].can_use()
