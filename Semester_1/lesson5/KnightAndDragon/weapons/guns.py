from .weapon import Weapon


class Bow(Weapon):
    def __init__(self, name, damage):
        super().__init__(name, damage)


class Crossbow(Weapon):
    def __init__(self, name, damage):
        super().__init__(name, damage)


class Staff(Weapon):
    def __init__(self, name, damage):
        super().__init__(name, damage)
