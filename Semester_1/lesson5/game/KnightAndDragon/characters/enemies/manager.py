from __future__ import annotations

import random

from .dragon import Dragon


class DragonManager:
    CLAWS_PHRASES = [
        "Дракон вонзил острые когти в '{target}'!",
        "'{target}' закричал от боли — когти дракона глубоко впились в плоть!",
        "Молниеносный удар когтями! '{target}' едва устоял на ногах.",
    ]

    TAIL_PHRASES = [
        "Оглушающий удар хвостом! '{target}' отброшен в сторону!",
        "'{target}' не успел увернуться — хвост дракона сбил его с ног!",
        "Дракон взмахнул хвостом, и '{target}' полетел через поле боя!",
    ]

    FIRE_BREATH_PHRASES = [
        "'{dragon}' вдохнул воздух и выпустил огненное дыхание на '{target}'!",
        "Поток пламени вырвался из пасти '{dragon}' и охватил '{target}'!",
        "'{dragon}' изверг огонь — '{target}' охвачен адским пламенем!",
    ]

    BURN_PHRASES = [
        "'{target}' истошно кричит — его пожирает огонь!",
        "Пламя не утихает — '{target}' продолжает гореть!",
        "Огненная боль терзает '{target}'!",
    ]

    def __init__(self, dragon: Dragon, custom_print):
        self._dragon = dragon
        self._custom_print = custom_print

    def next_turn(self, hero) -> None:
        """Выполняет один ход дракона против героя."""
        result = self._dragon.decide_and_act(hero)

        if result["type"] == "claws":
            msg = random.choice(self.CLAWS_PHRASES).format(
                target=str(hero), dragon=str(self._dragon)
            )
            self._custom_print(msg)
        elif result["type"] == "tail":
            msg = random.choice(self.TAIL_PHRASES).format(
                target=str(hero), dragon=str(self._dragon)
            )
            self._custom_print(msg)
        elif result["type"] == "fire_breath":
            msg = random.choice(self.FIRE_BREATH_PHRASES).format(
                target=str(hero), dragon=str(self._dragon)
            )
            self._custom_print(msg)

        # Если наложен поджог, то выводим дополнительную фразу
        if result["burn"]:
            self._custom_print(
                random.choice(self.BURN_PHRASES).format(target=str(hero))
            )
