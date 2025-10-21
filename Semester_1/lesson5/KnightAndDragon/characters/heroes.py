from typing import Dict

from .character import Character
from ..spells import Spell
from ..weapons import Weapon


class Hero(Character):
    def __init__(
            self,
            name: str,
            health: int,
            shield: int,
            damage: int,
            weapons: Dict[str, Weapon],
            spell: Spell,
    ):
        super().__init__(name, health, shield, damage)
        self._weapons: Dict[str, Weapon] = weapons
        self._spell: Spell = spell


class Knight(Hero):
    pass


class Wizard(Hero):
    pass


class Archer(Hero):
    pass


class Assassin(Hero):
    pass
