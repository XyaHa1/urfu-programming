class ArraySource:
    def __init__(self, arr):
        self.arr = arr
        self.index = 0

    def hasNext(self) -> bool:
        return self.index + 1 < len(self.arr)


    def next(self):
        if self.hasNext():
            self.index += 1
        else:
            raise StopIteration(f"")


    def peek(self) -> str:
        return self.arr[self.index]
