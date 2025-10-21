from .weapon import Weapon
from ..characters import Character


class Guns(Weapon):
    def __init__(self, name: str, damage: int, critical_chance, arrows: int):
        super().__init__(name, damage, critical_chance)
        self._arrows = arrows

    def attack(self, enemy: 'Character'):
        if self._arrows > 0:
            self._arrows -= 1
            return self._damage
        print("У вас закончились стрелы")
        return 0


class Bow(Guns):
    def __init__(self, name, damage, critical_chance, arrows):
        super().__init__(name, damage, critical_chance, arrows)


class Crossbow(Guns):
    def __init__(self, name, damage, critical_chance, arrows):
        super().__init__(name, damage, critical_chance, arrows)
