from abc import ABC, abstractmethod


class Character(ABC):
    def __init__(self, name: str, max_health: int, health: int, shield: int, damage: int):
        self._name: str = name
        self._max_health: int = max_health
        self._health: int = health
        self._shield: int = shield
        self._damage: int = damage

    def __str__(self) -> str:
        return self._name

    @property
    def max_health(self) -> int:
        return self._max_health

    @property
    def health(self) -> int:
        return self._health

    @property
    def shield(self) -> int:
        return self._shield

    @property
    def damage(self) -> int:
        return self._damage

    def is_alive(self) -> bool:
        return self._health > 0

    def take_damage(self, damage: int) -> None:
        if self._shield > 0:
            self._shield = max(self._shield - damage / 2, 0)
        else:
            self._health = max(self._health - damage, 0)

    @abstractmethod
    def attack_with_weapon(self, enemy: 'Character') -> None:
        pass

    @abstractmethod
    def attack_with_spell(self, enemy: 'Character') -> None:
        pass
