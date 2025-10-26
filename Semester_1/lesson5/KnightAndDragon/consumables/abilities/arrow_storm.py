from __future__ import annotations

from ..abilities import Ability


class ArrowStorm(Ability):
    def __init__(self, name, max_cost, cost, damage):
        super().__init__(name, max_cost, cost, damage)

    def apply(self, hero: "Hero", enemy: "Character") -> None:
        self._cost -= 1
        enemy.take_damage(self._damage * 3)
