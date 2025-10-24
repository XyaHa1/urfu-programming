import random
from abc import ABC


class Weapon(ABC):
    def __init__(self, name: str, damage: int, crit_chance: float):
        self._name: str = name
        self._damage: int = damage
        self._crit_chance: float = crit_chance

    def __str__(self) -> str:
        return self._name

    @property
    def damage(self) -> int:
        return self._damage

    def multiplier(self) -> float:
        if random.uniform(0, 1) <= self._crit_chance:
            return round(random.uniform(1, 2), 2)
        return 1.0
