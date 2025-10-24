from weapon import Weapon


class Bow(Weapon):
    def __init__(self, name, damage, crit_chance: float):
        super().__init__(name, damage, crit_chance)

class Crossbow(Weapon):
    def __init__(self, name, damage, crit_chance: float):
        super().__init__(name, damage, crit_chance)


class RangedStaff(Weapon):
    def __init__(self, name, damage, crit_chance: float):
        super().__init__(name, damage, crit_chance)
