from ..weapons.weapon import Weapon


class Bow(Weapon):
    def __init__(self, name, damage, crit_chance: float):
        super().__init__(name, damage, crit_chance)

    def type(self):
        return "ranged"


class Crossbow(Weapon):
    def __init__(self, name, damage, crit_chance: float):
        super().__init__(name, damage, crit_chance)

    def type(self):
        return "ranged"


class RangedStaff(Weapon):
    def __init__(self, name, damage, crit_chance: float):
        super().__init__(name, damage, crit_chance)

    def type(self):
        return "ranged"
