class StringSource:
    def __init__(self, string: str):
        if not isinstance(string, str):
            raise TypeError()
        self.string = string
        self.length = len(string)
        self.pos = 0

    def has_next(self) -> bool:
        return self.pos + 1 < self.length
    
    def peek(self) -> str:
        return self.string[self.pos]

    def next(self):
        self.pos += 1


class BaseParser:
    def __init__(self, source: StringSource):
        if not isinstance(source, StringSource):
            raise TypeError("Expected `StringSource`, but got: ", type(source))
        self.source = source

    def take(self):
        if self.source.has_next():
            self.source.next()
            return self.source.peek()
        raise StopIteration()


class StringCompressedParser(BaseParser):
    def __init__(self, source: StringSource):
        super().__init__(source)


def is_valid_compressed_string(compressed_string: str) -> bool:
    pass