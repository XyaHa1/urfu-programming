from __future__ import annotations

from ..abilities import Ability
from ..effects import ShieldingEffect


class Shielding(Ability):
    def __init__(self, name, max_cost, cost, damage=0):
        super().__init__(name, max_cost, cost, damage)

    def apply(self, hero: "Hero", enemy: "Character" = None) -> None:
        self._cost -= 1
        hero.add_effect(ShieldingEffect(self._name, 1))
