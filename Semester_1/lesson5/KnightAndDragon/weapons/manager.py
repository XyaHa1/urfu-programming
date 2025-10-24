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

    def damage(self) -> float:
        """
        Выполняет атаку текущим оружием.
        Выводит всё в консоль и возвращает урон.
        """
        weapon = self.get_current_weapon()
        multiplier = weapon.multiplier()

        if multiplier > 1.0:
            print(f"[Критический удар!] Урон увеличен на {multiplier * 100:.0f}%!")

        base = weapon.damage
        damage = base * multiplier
        print(f"[Урон] Вы нанесли {damage:.0f} единиц урона!")
        return damage
