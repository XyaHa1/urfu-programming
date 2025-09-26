from typing import List, Tuple
from Node import BinaryNode, UnaryNode, ConstantNode
from ArraySource import ArraySource


class DivisionByZeroError(Exception):
    pass


class BracketsError(Exception):
    pass


class Calculator:
    __expression: str
    __tokens: ArraySource

    def __init__(self):
        pass


    def evaluate(self, expression: str) -> float:
        pass


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
            elif ch in ('+', '-', '*', '/', '%'):
                if ch == '/' and i + 1 < length and exp[i + 1] == '/':
                    ch = '//'
                    i += 1
                arr.append(ch)
            elif ch != ' ':
                raise ValueError(f"Incorrect expression: pos = {i}")
            i += 1

        if brackets != 0:
            raise BracketsError("Incorrect bracket sequence")

        return arr


    # def __parse_expression(self):
    #     while self.__tokens.hasNext():
    #         pass
