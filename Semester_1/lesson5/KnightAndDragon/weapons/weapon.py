from ..characters import Character


class Weapon:
    def __init__(self, name, damage, critical_chance):
        self._name: str = name
        self._damage: int = damage
        self._critical_chance = critical_chance

    def __str__(self):
        return self._name

    def attack(self, enemy: 'Character'):
        pass
