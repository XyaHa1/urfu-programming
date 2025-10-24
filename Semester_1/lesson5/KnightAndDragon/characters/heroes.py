from abc import abstractmethod

from character import Character
from ..consumables import Ability
from ..consumables import PotionManager
from ..weapons import WeaponManager, Weapon


class Hero(Character):
    def __init__(
            self,
            name: str,
            max_health: int,
            health: int,
            shield: int,
            weapons_manager: WeaponManager,
            ability: Ability,
            potions_manager: PotionManager,
    ):
        super().__init__(name, max_health, health, shield)
        self._weapons_manager: WeaponManager = weapons_manager
        self._ability: Ability = ability
        self._potions_manager: PotionManager = potions_manager

    @property
    def weapon(self) -> Weapon:
        return self._weapons_manager.get_current_weapon()

    @weapon.setter
    def weapon(self, name_weapon: str) -> None:
        self._weapons_manager.switch_to(name_weapon)

    def attack(self, enemy: 'Character') -> float:
        damage = self._weapons_manager.damage()
        enemy.take_damage(damage)
        return damage

    def add_potion(self, name_potion: str, count: int = 1) -> None:
        self._potions_manager.add(name_potion, count)

    def use_potion(self, name_potion) -> None:
        self.health += self._potions_manager.use(name_potion)

    @abstractmethod
    def use_ability(self, enemy: 'Character') -> None:
        pass


class Knight(Hero):
    def __init__(
            self,
            name: str,
            max_health: int,
            health: int,
            shield: int,
            weapons_manager: WeaponManager,
            ability: Ability,
            potions_manager: PotionManager,
    ):
        super().__init__(
            name, max_health, health, shield, weapons_manager, ability, potions_manager
        )

    def use_ability(self, enemy: 'Character') -> None:
        pass


class Lumberjack(Hero):
    def __init__(
            self,
            name: str,
            max_health: int,
            health: int,
            shield: int,
            weapons_manager: WeaponManager,
            ability: Ability,
            potions_manager: PotionManager,
    ):
        super().__init__(
            name, max_health, health, shield, weapons_manager, ability, potions_manager
        )

    def use_ability(self, enemy: 'Character') -> None:
        pass


class Spearman(Hero):
    def __init__(
            self,
            name: str,
            max_health: int,
            health: int,
            shield: int,
            weapons_manager: WeaponManager,
            ability: Ability,
            potions_manager: PotionManager,
    ):
        super().__init__(
            name, max_health, health, shield, weapons_manager, ability, potions_manager
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
            weapons_manager: WeaponManager,
            ability: Ability,
            potions_manager: PotionManager,
    ):
        super().__init__(
            name, max_health, health, shield, weapons_manager, ability, potions_manager
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
            weapons_manager: WeaponManager,
            ability: Ability,
            potions_manager: PotionManager,
    ):
        super().__init__(
            name, max_health, health, shield, weapons_manager, ability, potions_manager
        )
        self._mana: int = mana

    @property
    def mana(self) -> int:
        return self._mana

    def use_ability(self, enemy: 'Character') -> None:
        pass

    def use_potion(self, name_potion) -> None:
        if name_potion == "health":
            self.health += self._potions_manager.use(name_potion)
        elif name_potion == "mana":
            self._mana += self._potions_manager.use(name_potion)


class Archer(Hero):
    def __init__(
            self,
            name: str,
            max_health: int,
            health: int,
            shield: int,
            weapons_manager: WeaponManager,
            ability: Ability,
            potions_manager: PotionManager,
    ):
        super().__init__(
            name, max_health, health, shield, weapons_manager, ability, potions_manager
        )

    def use_ability(self, enemy: 'Character') -> None:
        pass
