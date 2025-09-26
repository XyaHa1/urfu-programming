from abc import ABC, abstractmethod


class Node(ABC):
    @abstractmethod
    def evaluate(self) -> float:
        pass


class ConstantNode(Node):
    def __init__(self, value: float):
        self.value = value

    def evaluate(self) -> float:
        return self.value


class BinaryNode(Node):
    def __init__(self, left: Node, operator: str, right: Node):
        self.left = left
        self.operator = operator
        self.right = right

    def evaluate(self) -> float:
        operations: dict = {'+': lambda x, y: x + y,
                            '-': lambda x, y: x - y,
                            '*': lambda x, y: x * y,
                            '/': lambda x, y: x / y,
                            '//': lambda x, y: x // y,
                            '%': lambda x, y: x % y,
                            }

        return operations[self.operator](self.left.evaluate(), self.right.evaluate())


class UnaryNode(Node):
    def __init__(self, operator: str, operand: Node):
        self.operator = operator
        self.operand = operand

    def evaluate(self) -> float:
        operations: dict = {'-': lambda x: -x,
                            }

        return operations[self.operator](self.operand.evaluate())
