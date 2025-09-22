from collections import deque
from typing import List, Tuple


class DivisionByZeroError(Exception):
    pass


class BracketsError(Exception):
    pass


class Calculator:

    __expression: str
    __tokens: List[str]
    __pos: int

    def __init__(self):
        self.__evaluate: dict = {'+': lambda x, y: x + y,
                         '-': lambda x, y: x - y,
                         '*': lambda x, y: x * y,
                         '/': lambda x, y: x / y,
                         '//': lambda x, y: x // y,
                         '%': lambda x, y: x % y,
                                 }
        self.__priorities: dict = {'+': 1,
                                 '-': 1,
                                 '*': 2,
                                 '/': 2,
                                 '//': 2,
                                 '%': 2,
                                   }


    def eval(self, expression: str) -> float:
        self.__expression: str = expression
        self.__tokens: List[str] = self.__tokenize()
        self.__pos: int = 0

        return self.__parse_expression()



    def __parse_number(self, start: int, length: int) -> Tuple[str, int]:
            i = start
            exp = self.__expression
            while i < length and exp[i].isdigit():
                if exp[i].isdigit():
                    i += 1
                else:
                    break

            return exp[start:i], i - 1


    def __tokenize(self) -> List[str]:
        arr = []
        exp = self.__expression
        length = len(exp)
        i = 0
        brackets = 0
        while i < length:
            ch = exp[i]
            if ch.isdigit():
                num, i = self.__parse_number(i, length)
                arr.append(num)
            elif ch == '(':
                brackets += 1
                arr.append(ch)
            elif ch == ')':
                brackets -= 1
                arr.append(ch)
            elif self.__evaluate.get(ch):
                if ch == '/' and i + 1 < length and exp[i + 1] == '/':
                    ch = '//'
                    i += 1
                arr.append(ch)
            elif ch != ' ':
                raise ValueError("Incorrect expression")
            i += 1

        if brackets != 0:
            raise BracketsError("Incorrect bracket sequence")

        return arr


    def __parse_expression(self):
        ops: deque = deque()
        numbers: deque = deque()

        flag_priority_operator: bool = False
        unary_minus: bool = False

        while self.__pos < len(self.__tokens):
            t = self.__tokens[self.__pos]

            if t == '-' and (self.__pos == 0 or
                             self.__tokens[self.__pos - 1] == '(' or
                             self.__priorities.get(self.__tokens[self.__pos - 1], 0)):
                unary_minus = True
                self.__pos += 1
                continue

            if t.isdigit():
                num = float(t)
                if unary_minus:
                    num = -num
                    unary_minus = False
                numbers.append(num)

            elif t == '(':
                if self.__pos + 1 < len(self.__tokens):
                    self.__pos += 1
                    numbers.append(self.__parse_expression())
                else:
                    raise ValueError("Incorrect expression")

            elif t == ')':
                while len(ops) > 0:
                    n1 = numbers.popleft()
                    n2 = numbers.popleft()
                    numbers.appendleft(self.__evaluate[ops.popleft()](n1, n2))
                return numbers.pop()

            elif op := self.__priorities.get(t, 0):
                if op == 2:
                    flag_priority_operator = True
                ops.append(t)
                self.__pos += 1
                continue

            if flag_priority_operator:
                n2 = numbers.pop()
                n1 = numbers.pop()
                op = ops.pop()
                if op in ('/', '//', '%') and n2 == 0:
                    raise DivisionByZeroError("Division by zero")
                numbers.append(self.__evaluate[op](n1, n2))
                flag_priority_operator = False

            self.__pos += 1

        while len(ops) > 0:
            n1 = numbers.popleft()
            n2 = numbers.popleft()
            numbers.appendleft(self.__evaluate[ops.popleft()](n1, n2))

        return numbers[0]




if __name__ == '__main__':
    c = Calculator()
    print(c.eval('( ( 1    +   2   *  '
                 '  (  3    / (9 *    7 - (98 / 12 -6    )    ) *    4   ) / 7 '
                 '- 5 * 6 + (6 - 7 * (10 + (8 / (6 '
                 '- - 4 )  )   )- 8) '
                 '   ))  '))
