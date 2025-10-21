from .weapon import Weapon


class Sword(Weapon):
    def __init__(self, damage: int, critical_chance):
        super().__init__(damage, critical_chance)


class Axe(Weapon):
    def __init__(self, damage, critical_chance):
        super().__init__(damage, critical_chance)

    def attack(self):
        pass


class Knife(Weapon):
    def __init__(self, damage, critical_strike):
        super().__init__(damage, critical_strike)

    def attack(self):
        pass
