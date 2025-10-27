from ..weapons.weapon import Weapon


class Sword(Weapon):
    def __init__(self, name: str, damage: int, crit_chance: float):
        super().__init__(name, damage, crit_chance)

    def type(self):
        return "melee"


class Axe(Weapon):
    def __init__(self, name: str, damage, crit_chance: float):
        super().__init__(name, damage, crit_chance)

    def type(self):
        return "melee"


class Knife(Weapon):
    def __init__(self, name: str, damage, crit_chance: float):
        super().__init__(name, damage, crit_chance)

    def type(self):
        return "melee"


class Spear(Weapon):
    def __init__(self, name: str, damage, crit_chance: float):
        super().__init__(name, damage, crit_chance)

    def type(self):
        return "melee"


class MeleeStaff(Weapon):
    def __init__(self, name: str, damage, crit_chance: float):
        super().__init__(name, damage, crit_chance)

    def type(self):
        return "melee"
