from .effect import Effect


class BurnEffect(Effect):
    def __init__(self, name, damage, duration):
        super().__init__(name, duration)
        self.damage_per_turn = damage

    def apply(self, target) -> None:
        target.take_damage(self.damage_per_turn)
