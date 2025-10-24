from typing import Dict

from weapon import Weapon


class WeaponManager:
    def __init__(self, weapons: Dict[str, Weapon]):
        self._weapons = weapons
        self._current_weapon_name: str = next(iter(weapons.keys()))

    def get_current_weapon(self) -> Weapon:
        return self._weapons[self._current_weapon_name]
