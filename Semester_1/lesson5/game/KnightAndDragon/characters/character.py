from __future__ import annotations

from abc import ABC
from typing import List

from ..consumables import EffectManager
from ..utils import custom_output


class Character(ABC):
    def __init__(
            self,
            name: str,
            max_health: int,
            health: int,
            shield: int,
            effect_manager: "EffectManager" = EffectManager(custom_output),
    ):
        self._name: str = name
        self._max_health: int = max_health
        self._health: int = health
        self._shield: int = shield
        self._active_effect: List["Effect"] = []
        self._effect_manager: "EffectManager" = effect_manager

    def __str__(self) -> str:
        return self._name

    @property
    def max_health(self) -> int:
        return self._max_health

    @property
    def health(self) -> int:
        return self._health

    @health.setter
    def health(self, health: int) -> None:
        self._health = min(self._max_health, self._health + health)

    @property
    def shield(self) -> float:
        return self._shield

    def is_alive(self) -> bool:
        return self._health > 0

    def take_damage(self, damage: float) -> None:
        for effect in self._active_effect:
            if str(effect) == "Щит":
                effect.consume()
                self._effect_manager.on_effect(self, effect)
                self._active_effect.remove(effect)
                return

        if self._shield > 0:
            preprocessing_damage = self._shield - damage / 2
            if preprocessing_damage < 0:
                normalize_damage = abs(preprocessing_damage) * 2
                self._health = self._health - normalize_damage
            self._shield = round(max(preprocessing_damage, 0), 2)
        else:
            self._health = round(max(self._health - damage, 0), 2)

    def add_effect(self, effect: "Effect") -> None:
        for effect_exist in self._active_effect:
            if str(effect_exist) == str(effect):
                effect_exist.description = effect.description
                return
        self._active_effect.append(effect)

    def process_effect(self, enemy) -> None:
        for effect in reversed(self._active_effect):
            effect.tick(self)
            self._effect_manager.on_effect(self, enemy, effect)
            if effect.description <= 0 and str(effect) != "Щит":
                self._active_effect.remove(effect)
