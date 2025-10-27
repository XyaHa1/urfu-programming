from .effect import Effect


class BleedEffect(Effect):
    def __init__(self, name, damage, duration):
        super().__init__(name, duration)
        self._damage = damage

    def apply(self, target) -> None:
        target.take_damage(self._damage)
