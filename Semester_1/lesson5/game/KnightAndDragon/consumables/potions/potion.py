class Potion:
    def __init__(self, name: str, max_count: int, value: int):
        self._name: str = name
        self._max_count: int = max_count
        self._current_count: int = max_count
        self._value: int = value

    @property
    def max_count(self):
        return self._max_count

    @property
    def current_count(self):
        return self._current_count

    @property
    def value(self):
        return self._value

    def __str__(self):
        return f"{self._name}"

    def add(self, count=1) -> int:
        added = min(count, self._max_count - self._current_count)
        self._current_count += added
        return added

    def use(self) -> int:
        self._current_count -= 1
        return self._value

    def can_use(self) -> bool:
        return self._current_count > 0
