from __future__ import annotations

import random
from typing import Dict

from ..potions.potion import Potion


class PotionManager:
    _NARRATOR_HEALING_PHRASES = [
        "'{user}' поднёс к губам пузырёк с целебной жидкостью. Тепло разлилось по телу — здоровье восстановлено на {amount} единиц.",
        "Глоток зелья — и раны начали затягиваться. '{user}' чувствует, как силы возвращаются (+{amount} HP).",
        "Целебная магия влилась в жилы '{user}'. {amount} жизненных сил возвращены.",
        "Пузырёк разбился в ладони — и туман исцеления окутал '{user}'. Здоровье восстановлено.",
    ]

    def __init__(self, name_user: str, potions: Dict[str, Potion], custom_print=None):
        self._potions = potions
        self._name_user = name_user
        self._custom_print = custom_print

    def use(self, potion_name) -> int:
        potion = self._potions.get(potion_name)
        if potion.can_use():
            potion_value = potion.use()
            if potion_name == "Лечебное зелье":
                self._custom_print(
                    random.choice(self._NARRATOR_HEALING_PHRASES).format(
                        user=self._name_user, amount=potion_value
                    )
                )
            elif potion_name == "Эликсир маны":
                pass
            return potion_value
        self._custom_print(
            f"К сожалению, у '{self._name_user}' нет '{potion_name}' для использования"
        )
        return 0

    def add(self, potion_name: str, count: int = 1) -> None:
        potion = self._potions.get(potion_name)
        added = potion.add(count)
        if added > 0:
            self._custom_print(
                f"Отлично, теперь у '{self._name_user}' {self._potions[potion_name].current_count} из {self._potions[potion_name].max_count} шт. '{potion_name}'!"
            )
            return

        self._custom_print(
            f"Очень жаль, но у {self._name_user} больше нет места для '{potion_name}'."
        )
