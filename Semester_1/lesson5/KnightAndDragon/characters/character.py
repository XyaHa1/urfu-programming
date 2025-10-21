class Character:
    def __init__(self, name: str, health: int, shield: int, damage: int):
        self._name: str = name
        self._health: int = health
        self._shield: int = shield
        self._damage: int = damage

    def __str__(self) -> str:
        return self._name

    def attack(self, enemy: 'Character') -> None:
        pass
