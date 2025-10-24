from typing import Dict

from weapon import Weapon


class WeaponManager:
    def __init__(self, weapons: Dict[str, Weapon]):
        self._weapons = weapons
        self._current_weapon_name: str = next(iter(weapons.keys()))

    def get_current_weapon(self) -> Weapon:
        return self._weapons[self._current_weapon_name]

    def switch_to(self, name: str) -> None:
        """Переключает оружие и выводит сообщение."""
        if name not in self._weapons:
            print(f"*У меня нет оружия '{name}'*")
            return

        if name == self._current_weapon_name:
            print(f"*Я уже использую {name}.*")
            return

        self._current_weapon_name = name
        print(f"*Вы экипировали: {name}*")
