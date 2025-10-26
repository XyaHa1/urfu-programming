import random
from typing import Dict

from ..weapons.weapon import Weapon


class WeaponManager:
    NARRATOR_MELEE_PHRASES = [
        "'{user}' взмахнул '{weapon}' — и воздух рассёкся от силы удара. Враг пошатнулся, получив {damage:.0f} урона.",
        "'{weapon}' сверкнул в свете заката. Враг почувствовал боль — {damage:.0f} жизненных сил ушло в никуда.",
        "Без крика, без предупреждения — '{user}' нанёс удар. Противник теряет {damage:.0f} здоровья.",
        "Сталь зазвенела, встречая плоть. Противник получил {damage:.0f} урона — и это лишь начало.",
    ]

    NARRATOR_RANGED_PHRASES = [
        "Снаряд '{user}' сорвалась с '{weapon}' — и в следующее мгновение вонзилась во врага. Урон: {damage:.0f}.",
        "Снаряд вылетел из '{weapon}' '{user}' и нашёл свою цель. Враг почувствовал, как боль пронзает тело.",
        "На расстоянии '{user}' смертоносен. Злодей получил {damage:.0f} урона — и не видел, откуда пришла смерть.",
    ]

    def __init__(self, name_user: str, weapons: Dict[str, Weapon], custom_print=None):
        self._name_user = name_user
        self._weapons = weapons
        self._current_weapon_name: str = next(iter(weapons.keys()))
        self._custom_print = custom_print

    def get_current_weapon(self) -> Weapon:
        """Выдает текущее оружие."""
        return self._weapons[self._current_weapon_name]

    def get_damage_weapon(self) -> int:
        """Выдает урон текущего оружия."""
        return self._weapons[self._current_weapon_name].damage

    def switch_to(self, name: str) -> None:
        """Переключает оружие и выводит сообщение."""
        if name not in self._weapons:
            self._custom_print(f"У {self._name_user} нет оружия '{name}'.")
            return

        if name == self._current_weapon_name:
            self._custom_print(f"{self._name_user} уже использует {name}.")
            return

        self._current_weapon_name = name
        self._custom_print(
            f"Теперь '{self._name_user}' использует {name}. Врагу следует бежать!"
        )

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
        if weapon.type() == "melee":
            self._custom_print(
                random.choice(self.NARRATOR_MELEE_PHRASES).format(
                    user=self._name_user, damage=damage, weapon=str(weapon)
                )
            )
        elif weapon.type() == "ranged":
            self._custom_print(
                random.choice(self.NARRATOR_RANGED_PHRASES).format(
                    user=self._name_user, damage=damage, weapon=str(weapon)
                )
            )
        return damage
