from __future__ import annotations

from random import random

from ..character import Character
from ...consumables.effects import BurnEffect


class Dragon(Character):
    """
    Методы возвращают словарь с результатом действия
    для дальнейшей обработки в DragonManager.
    Индивидуально реализует действия без привязки к
    вспомогательным классам героя.
    """

    def __init__(
            self,
            name: str,
            max_health: int,
            health: int,
            shield: int,
            claw_damage: int,
            tail_damage: int,
            fire_breath_damage: int,
            fire_breath_burn_damage: int = 10,
            fire_breath_burn_duration: int = 3,
            ability_chance: float = 0.3,
    ):
        super().__init__(name, max_health, health, shield)
        self._claw_damage = claw_damage
        self._tail_damage = tail_damage
        self._fire_breath_damage = fire_breath_damage
        self._fire_breath_burn_damage = fire_breath_burn_damage
        self._fire_breath_burn_duration = fire_breath_burn_duration
        self._ability_chance = ability_chance

    def attack_claws(self, enemy: Character) -> dict:
        enemy.take_damage(self._claw_damage)
        applied_burn = False
        if random() < 0.25:  # 25% шанс поджога от когтей
            enemy.add_effect(BurnEffect(name="Огненное пламя", damage=6, duration=2))
            applied_burn = True
        return {"type": "claws", "damage": self._claw_damage, "burn": applied_burn}

    def attack_tail(self, enemy: Character) -> dict:
        enemy.take_damage(self._tail_damage)
        return {"type": "tail", "damage": self._tail_damage, "burn": False}

    def use_fire_breath(self, enemy: Character) -> dict:
        enemy.take_damage(self._fire_breath_damage)
        enemy.add_effect(
            BurnEffect(
                name="Огненное пламя",
                damage=self._fire_breath_burn_damage,
                duration=self._fire_breath_burn_duration,
            )
        )
        return {"type": "fire_breath", "damage": self._fire_breath_damage, "burn": True}

    def decide_and_act(self, enemy: Character) -> dict:
        """
        Принимает решение: атака (когти/хвост) или способность.
        Возвращает результат действия.
        """
        if random() < self._ability_chance:
            return self.use_fire_breath(enemy)
        if random() < 0.5:
            return self.attack_claws(enemy)
        return self.attack_tail(enemy)
