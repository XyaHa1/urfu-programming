from __future__ import annotations

from abc import ABC, abstractmethod


class Effect(ABC):
    def __init__(self, name, duration):
        self._name = name
        self._duration = duration

    def __str__(self):
        return self._name

    @property
    def description(self):
        return self._duration

    @description.setter
    def description(self, value):
        self._duration = value

    @abstractmethod
    def apply(self, character) -> None:
        pass

    def tick(self, character) -> None:
        self.apply(character)
        self._duration -= 1
