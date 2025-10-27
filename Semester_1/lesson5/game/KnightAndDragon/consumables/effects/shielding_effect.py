from ..effects import Effect


class ShieldingEffect(Effect):
    def __init__(self, name, duration):
        super().__init__(name, duration)

    def apply(self, target=None) -> None:
        pass

    def consume(self) -> None:
        self._duration = 0
