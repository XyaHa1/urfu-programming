from abc import ABC


class Ability(ABC):
    def __init__(self, description, max_cost, cost, damage):
        self._description = description
        self._max_cost = max_cost
        self._cost = cost
        self._damage = damage
