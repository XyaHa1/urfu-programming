from __future__ import annotations

from abc import ABC, abstractmethod


class Ability(ABC):
    def __init__(self, name, max_cost, cost, damage):
        self._name = name
        self._max_cost = max_cost
        self._cost = cost
        self._damage = damage

    def __str__(self):
        return self._name

    @property
    def cost(self):
        return self._cost

    @property
    def max_cost(self):
        return self._max_cost

    def can_use(self):
        return self._cost > 0

    @abstractmethod
    def apply(self, hero: "Hero", enemy: "Character") -> None:
        pass
