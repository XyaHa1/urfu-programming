from weapon import Weapon


class Sword(Weapon):
    def __init__(self, name: str, damage: int, crit_chance: float):
        super().__init__(name, damage, crit_chance)


class Axe(Weapon):
    def __init__(self, name: str, damage, crit_chance: float):
        super().__init__(name, damage, crit_chance)


class Knife(Weapon):
    def __init__(self, name: str, damage, crit_chance: float):
        super().__init__(name, damage, crit_chance)


class Spear(Weapon):
    def __init__(self, name: str, damage, crit_chance: float):
        super().__init__(name, damage, crit_chance)


class MeleeStaff(Weapon):
    def __init__(self, name: str, damage, crit_chance: float):
        super().__init__(name, damage, crit_chance)
