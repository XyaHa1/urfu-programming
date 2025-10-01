from typing import TypeVar, List
from enum import Enum

from visualization import *


class Result(Enum):
    CORRECT = 1,
    INCORRECT = 2,
    NO_LETTER = 3,
    REPEAT = 4


step = TypeVar('step')
class Game:
    _word: str
    _letters: dict[str, bool]
    _letters_used: List[bool]
    _steps: List[step]

    def __init__(self):
        self._letters = {chr(i): False for i in range(ord('А'), ord('Я') + 1)}
        self._steps = [step_1(), step_2(), step_3(),
                       step_4(), step_5(), step_6(),
                       step_7(), step_8(), step_9(),
                       step_10(), step_11()]


    def _examination(self, letter: str) -> Result:
        if letter not in self._letters:
            return Result.NO_LETTER

        if self._letters[letter] is True:
            return Result.REPEAT

        self._letters[letter] = True
        flag: int = 0
        for i in range(len(self._word)):
            if letter == self._word[i]:
                self._letters_used[i] = True
                flag += 1

        return Result.CORRECT if flag != 0 else Result.INCORRECT


    def _show_word(self):
        print('[>] ', end='')
        for i in range(len(self._word)):
            if self._letters_used[i]:
                print(self._word[i], end=' ')
            else:
                print('_', end=' ')
        print('\n')


    def _is_win(self) -> bool:
        for l in range(len(self._word)):
            if self._letters_used[l] is False:
                return False

        return True


    def play(self):
        print(show_start())
        show_menu()

        self._word = input('[>] Введите слово: ').strip().upper()
        self._letters_used = [False] * len(self._word)

        index_step: int = 0
        while True:
            letter = input('[>] Введите букву: ').strip().upper()
            result: Result = self._examination(letter)

            match result:
                case Result.CORRECT:
                    print('[!] Правильная буква!\n')
                case Result.INCORRECT:
                    print('[!] Неправильная буква!\n')
                    print(self._steps[index_step])
                    index_step += 1
                case Result.NO_LETTER:
                    print('[?] В алфавите такой буквы нет')
                case Result.REPEAT:
                    print('[!] Буква уже была!')

            self._show_word()

            if self._is_win():
                print('[=] Поздравляем, вы выиграли! :)\n')
                break

            if index_step == 11:
                print(f'[=] Вы проиграли ;(\n')
                break
