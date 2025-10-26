from __future__ import annotations

import random
from typing import List

from ..abilities import Ability


class AbilityManager:
    def __init__(self, ability: Ability, msg: List[str], custom_print=None):
        self._ability = ability
        self._msg = msg
        self._custom_print = custom_print

    def _can_use(self, hero: 'Hero'):
        if not self._ability.can_use():
            self._custom_print(f"'{str(hero)}' больше не может использовать '{self._ability}'")
            return False
        return True

    def apply(self, hero, character):
        if self._can_use(hero):
            self._ability.apply(hero, character)
            if str(self._ability) == 'Щит':
                return
            self._custom_print(
                random.choice(self._msg).format(user=str(hero), target=str(character))
            )
