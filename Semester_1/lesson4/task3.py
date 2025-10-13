from enum import Enum
from typing import List


class Side(Enum):
    LEFT = 1
    RIGHT = 2
    LEFT_RIGHT = 3


def side_of_string(new_s: List[str], 
                   target: str, 
                   count_target_symbol: int, 
                   side: Side):
    target_str: str  = target * count_target_symbol
    new_string: str = ''.join(new_s)

    if side == Side.LEFT:
        new_string = target_str + new_string
    elif side == Side.RIGHT:
        new_string = new_string + target_str
    elif side == Side.LEFT_RIGHT:
        new_string = target_str + new_string + target_str
    
    return new_string
        


def permutation_symbols(s: str, target: str, side: Side):
    count_target_symbol = 0
    new_string = []
    for ch in s:
        if ch == target:
            count_target_symbol += 1
        else:
            new_string.append(ch)
        
    return side_of_string(new_string, target, count_target_symbol, side)


if __name__ == '__main__':
    while True:
        s = input('[>] Введите строку: ')
        target = input('[>] Введите символ: ')
        print('1. Левый\n'
              '2. Правый\n'
              '3. Левый и Правый')
        side = Side(int(input('[>] Выберите сторону: ')))
        print(permutation_symbols(s, target, side))