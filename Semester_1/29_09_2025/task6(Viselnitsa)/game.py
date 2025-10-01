from typing import TypeVar, List
from enum import Enum

from visualization import *


class Result(Enum):
    CORRECT = 1
    INCORRECT = 2
    NO_LETTER = 3
    REPEAT = 4


step = TypeVar('step')
class Game:
    __word: str
    __letters: dict[str, bool]
    __letters_used: List[bool]
    __steps: List[step]

    def __init__(self):
        self.__letters = {chr(i): False for i in range(ord('А'), ord('Я') + 1)}
        self.__steps = [step_1(), step_2(), step_3(),
                        step_4(), step_5(), step_6(),
                        step_7(), step_8(), step_9(),
                        step_10(), step_11()]


    def __validate_letter(self, letter: str) -> bool:
        return len(letter) == 1 and letter in self.__letters


    def __examination(self, letter: str) -> Result:
        if not self.__validate_letter(letter):
            return Result.NO_LETTER

        if self.__letters[letter] is True:
            return Result.REPEAT

        self.__letters[letter] = True
        flag: int = 0
        for i in range(len(self.__word)):
            if letter == self.__word[i]:
                self.__letters_used[i] = True
                flag += 1

        return Result.CORRECT if flag != 0 else Result.INCORRECT


    def __show_word(self):
        s = []
        for i in range(len(self.__word)):
            if self.__letters_used[i]:
                s.append(self.__word[i])
            else:
                s.append('_')

        print(f'[>] {" ".join(s)}')


    def __is_win(self) -> bool:
        return all(self.__letters_used)


    def __is_lose(self, index_steps: int) -> bool:
        return index_steps >= len(self.__steps)


    def play(self):
        print(show_start())
        show_menu()

        while True:
            self.__word = input('[>] Введите слово: ').strip().upper()
            if self.__word != '' and all(ch in self.__letters for ch in self.__word):
                break
            else:
                print('[!] Введите слово корректное слово для русского алфавита.\n')

        self.__letters_used = [False] * len(self.__word)

        index_step: int = 0
        while True:
            letter = input('[>] Введите букву: ').strip().upper()
            result: Result = self.__examination(letter)

            match result:
                case Result.CORRECT:
                    print('[!] Правильная буква!\n')
                case Result.INCORRECT:
                    print(f'[!] Неправильная буква!\n')
                    print(self.__steps[index_step])
                    print(f'[!] Ошибок: {index_step + 1}/{len(self.__steps)}')
                    index_step += 1
                case Result.NO_LETTER:
                    print('[?] В русском алфавите нет такой буквы.\n')
                case Result.REPEAT:
                    print('[!] Эта буква уже была использована!\n')

            self.__show_word()

            if self.__is_win():
                print('[=] Поздравляем, вы выиграли! :)\n')
                break

            if self.__is_lose(index_step):
                print(f'\n[=] Вы проиграли ;(\n'
                      f'[>] Загаданное слово: {self.__word}')
                break
