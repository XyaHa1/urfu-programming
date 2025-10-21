from abc import ABC


class Weapon(ABC):
    def __init__(self, name, damage):
        self._name: str = name
        self._damage: int = damage

    @property
    def damage(self):
        return self._damage

    def __str__(self):
        return self._name
