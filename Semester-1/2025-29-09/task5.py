from typing import List


arabic_romes = [(1000, 'M'), (900, 'CM'), (500, 'D'),
                (400, 'CD'), (100, 'C'), (90, 'XC'),
                (50, 'L'), (40, 'XL'), (10, 'X'),
                (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')]


def converter_arabic_to_romes(number: int) -> str:
    if number < 1:
        ValueError(f'Expected number > 0, got {number}')

    result: List[str] = []
    for arabic, rome in arabic_romes:
        if number >= arabic:
            count = number // arabic
            number %= arabic
            result += rome * count

    return ''.join(result)


def converter_romes_to_arabic(number: str) -> int:
    result = 0
    for arabic, rome in arabic_romes:
        while number.startswith(rome):
            result += arabic
            number = number[len(rome):]

        if len(number) == 0:
            return result

    return result


if __name__ == '__main__':

    """
        Ожидается корректный ввод чисел!
    """

    n = input('==========================\n'
              ' Конвертер римских чисел\n'
              '==========================\n\n'
              '[!] Введите число: ')
    if n.isdigit():
        r = converter_arabic_to_romes(int(n))
        print(f'[+] Число {n} в римской системе: {r}\n')
    else:
        r = converter_romes_to_arabic(n)
        print(f'[+] Число {n} в арабской системе: {r}\n')
