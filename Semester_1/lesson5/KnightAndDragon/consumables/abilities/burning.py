from __future__ import annotations

from ..abilities import Ability
# from ...characters import Character, Hero
from ..effects import BurnEffect


class Burning(Ability):
    def __init__(self, name, max_cost, cost, damage):
        super().__init__(name, max_cost, cost, damage)

    def apply(self, hero: "Hero", enemy: "Character") -> None:
        self._cost -= 1
        enemy.take_damage(self._damage)
        enemy.add_effect(BurnEffect(name=self._name, damage=self._damage, duration=self._max_cost - 1))
