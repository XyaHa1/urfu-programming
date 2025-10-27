from __future__ import annotations

from ..character import Character


class Hero(Character):
    def __init__(
            self,
            name: str,
            max_health: int,
            health: int,
            shield: int,
            weapons_manager: "WeaponManager",
            ability: "AbilityManager",
            potions_manager: "PotionManager",
    ):
        super().__init__(name, max_health, health, shield)
        self._weapons_manager: "WeaponManager" = weapons_manager
        self._ability: "AbilityManager" = ability
        self._potions_manager: "PotionManager" = potions_manager

    @property
    def weapon(self) -> "Weapon":
        return self._weapons_manager.get_current_weapon()

    def switch_weapon(self, name_weapon: str) -> None:
        self._weapons_manager.switch_to(name_weapon)

    def get_damage_from_weapon(self) -> int:
        return self._weapons_manager.get_damage_weapon()

    def attack(self, enemy: "Character") -> float:
        damage = self._weapons_manager.damage()
        enemy.take_damage(damage)
        return damage

    def add_potion(self, name_potion: str, count: int = 1) -> None:
        self._potions_manager.add(name_potion, count)

    def use_potion(self, name_potion) -> None:
        self._health += self._potions_manager.use(name_potion)

    def can_use_ability(self) -> bool:
        return self._ability.can_use(self)

    def use_ability(self, enemy: "Character") -> None:
        self._ability.apply(self, enemy)


class Knight(Hero):
    def __init__(
            self,
            name: str,
            max_health: int,
            health: int,
            shield: int,
            weapons_manager: "WeaponManager",
            ability: "AbilityManager",
            potions_manager: "PotionManager",
    ):
        super().__init__(
            name,
            max_health,
            health,
            shield,
            weapons_manager,
            ability,
            potions_manager,
        )


class Lumberjack(Hero):
    def __init__(
            self,
            name: str,
            max_health: int,
            health: int,
            shield: int,
            weapons_manager: "WeaponManager",
            ability: "AbilityManager",
            potions_manager: "PotionManager",
    ):
        super().__init__(
            name,
            max_health,
            health,
            shield,
            weapons_manager,
            ability,
            potions_manager,
        )


class Spearman(Hero):
    def __init__(
            self,
            name: str,
            max_health: int,
            health: int,
            shield: int,
            weapons_manager: "WeaponManager",
            ability: "AbilityManager",
            potions_manager: "PotionManager",
    ):
        super().__init__(
            name,
            max_health,
            health,
            shield,
            weapons_manager,
            ability,
            potions_manager,
        )


class Assassin(Hero):
    def __init__(
            self,
            name: str,
            max_health: int,
            health: int,
            shield: int,
            weapons_manager: "WeaponManager",
            ability: "AbilityManager",
            potions_manager: "PotionManager",
    ):
        super().__init__(
            name,
            max_health,
            health,
            shield,
            weapons_manager,
            ability,
            potions_manager,
        )


class Wizard(Hero):
    def __init__(
            self,
            name: str,
            max_health: int,
            health: int,
            mana: int,
            shield: int,
            weapons_manager: "WeaponManager",
            ability: "AbilityManager",
            potions_manager: "PotionManager",
    ):
        super().__init__(
            name,
            max_health,
            health,
            shield,
            weapons_manager,
            ability,
            potions_manager,
        )
        self._mana: int = mana

    @property
    def mana(self) -> int:
        return self._mana

    def use_potion(self, name_potion) -> None:
        if name_potion == "Лечебное зелье":
            self.health += self._potions_manager.use(name_potion)
        elif name_potion == "Эликсир маны":
            self._mana += self._potions_manager.use(name_potion)


class Archer(Hero):
    def __init__(
            self,
            name: str,
            max_health: int,
            health: int,
            shield: int,
            weapons_manager: "WeaponManager",
            ability: "AbilityManager",
            potions_manager: "PotionManager",
    ):
        super().__init__(
            name,
            max_health,
            health,
            shield,
            weapons_manager,
            ability,
            potions_manager,
        )
