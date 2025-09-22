from collections import deque
from typing import List, Tuple


class DivisionByZeroError(Exception):
    pass


class BracketsError(Exception):
    pass


class Calculator:
    def __init__(self, expression):
        self.stack = deque()
        self.expression = expression
        self.evaluate = {'+': lambda x, y: x + y,
                         '-': lambda x, y: x - y,
                         '*': lambda x, y: x * y,
                         '/': lambda x, y: x / y,
                         '//': lambda x, y: x // y,
                         '%': lambda x, y: x % y
                         }

        self.tokens = self.tokenize()


    def parse_number(self, start: int, length: int) -> Tuple[str, int]:
            i = start
            exp = self.expression
            while i < length and exp[i].isdigit():
                if exp[i].isdigit():
                    i += 1
                else:
                    break

            return exp[start:i], i - 1


    def tokenize(self) -> List[str]:
        arr = []
        exp = self.expression
        length = len(exp)
        i = 0
        brackets = 0
        while i < length:
            ch = exp[i]
            if ch.isdigit():
                num, i = self.parse_number(i, length)
                arr.append(num)
            elif ch == '(':
                brackets += 1
                arr.append(ch)
            elif ch == ')':
                brackets -= 1
                arr.append(ch)
            elif ch in self.evaluate.keys():
                arr.append(ch)
            i += 1

        if brackets != 0:
            raise BracketsError("Incorrect bracket sequence")

        return arr


if __name__ == '__main__':
    c = Calculator('   1    +   2   *    (  3   '
                   ' + 4   )')
    print(c.tokens)
    # print(c.tokenize())