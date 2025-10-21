from .weapon import Weapon


class Sword(Weapon):
    def __init__(self, name: str, damage: int):
        super().__init__(name, damage)


class Axe(Weapon):
    def __init__(self, name: str, damage):
        super().__init__(name, damage)


class Knife(Weapon):
    def __init__(self, name: str, damage):
        super().__init__(name, damage)
