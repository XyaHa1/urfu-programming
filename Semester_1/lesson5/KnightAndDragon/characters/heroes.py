import random
from abc import abstractmethod
from typing import Dict, Union

from .character import Character
from ..consumables import Ability
from ..consumables import PotionManager
from ..weapons import Weapon

_HeroPotionType = Union["health"]
_WizardPotionType = Union["health", "mana"]

class Hero(Character):
    def __init__(
            self,
            name: str,
            max_health: int,
            health: int,
            shield: int,
            damage: int,
            weapons: Dict[str, Weapon],
            ability: Ability,
            potions_manager: PotionManager,
    ):
        super().__init__(name, max_health, health, shield, damage)
        self._weapons: Dict[str, Weapon] = weapons
        # Выбираем первое оружие по умолчанию
        self._weapon: Weapon = next(iter(weapons.values()))
        self._ability: Ability = ability
        self._potions_manager: PotionManager = potions_manager

    @property
    def weapon(self) -> Weapon:
        return self._weapon

    @weapon.setter
    def weapon(self, name_weapon: str) -> None:
        self._weapon = self._weapons.get(name_weapon, self._weapon)

    def attack(self, enemy: 'Character') -> int:
        multiplier = 1
        if random.uniform(0, 1) <= 0.2:
            multiplier = random.uniform(1, 2)
        enemy.take_damage((self._weapon.damage + self._damage) * multiplier)
        return (self._weapon.damage + self._damage) * multiplier

    def add_potion(self, name_potion: str, count: int = 1) -> None:
        self._potions_manager.add(name_potion, count)

    @abstractmethod
    def use_ability(self, enemy: 'Character') -> None:
        pass

    def use_potion(self, name_potion: _HeroPotionType) -> None:
        self.health += self._potions_manager.use(name_potion)


class Knight(Hero):
    def __init__(
            self,
            name: str,
            max_health: int,
            health: int,
            shield: int,
            damage: int,
            weapons: Dict[str, Weapon],
            ability: Ability,
            potions_manager: PotionManager,
    ):
        super().__init__(
            name, max_health, health, shield, damage, weapons, ability, potions_manager
        )

    def use_ability(self, enemy: 'Character') -> None:
        pass


class Wizard(Hero):
    def __init__(
            self,
            name: str,
            max_health: int,
            health: int,
            mana: int,
            shield: int,
            damage: int,
            weapons: Dict[str, Weapon],
            ability: Ability,
            potions_manager: PotionManager,
    ):
        super().__init__(
            name, max_health, health, shield, damage, weapons, ability, potions_manager
        )
        self._mana: int = mana

    @property
    def mana(self) -> int:
        return self._mana

    @mana.setter
    def mana(self, value: int) -> None:
        self._mana += value

    def use_ability(self, enemy: 'Character') -> None:
        pass

    def use_potion(self, name_potion: _WizardPotionType) -> None:
        if name_potion == "health":
            self.health += self._potions_manager.use(name_potion)
        elif name_potion == "mana":
            self.mana += self._potions_manager.use(name_potion)


class Archer(Hero):
    def __init__(
            self,
            name: str,
            max_health: int,
            health: int,
            shield: int,
            damage: int,
            weapons: Dict[str, Weapon],
            ability: Ability,
            potions_manager: PotionManager,
    ):
        super().__init__(
            name, max_health, health, shield, damage, weapons, ability, potions_manager
        )

    def use_ability(self, enemy: 'Character') -> None:
        pass


class Assassin(Hero):
    def __init__(
            self,
            name: str,
            max_health: int,
            health: int,
            shield: int,
            damage: int,
            weapons: Dict[str, Weapon],
            ability: Ability,
            potions_manager: PotionManager,
    ):
        super().__init__(
            name, max_health, health, shield, damage, weapons, ability, potions_manager
        )

    def use_ability(self, enemy: 'Character') -> None:
        pass
