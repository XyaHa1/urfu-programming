class StringSource:
    def __init__(self, string: str):
        if not isinstance(string, str):
            raise TypeError("Expected `str`, but got: ", type(string), f"with value: {string}")
        self.string = string
        self.length = len(string)
        self.pos = 0

    def has_next(self) -> bool:
        return self.pos < self.length
    
    def peek(self) -> str:
        return self.string[self.pos]

    def next(self):
        self.pos += 1

    def error(self, msg: str):
        raise ValueError(f'Expected: `"{msg}"`, but got: `"{self.peek()}"` at position: {self.pos}')


class BaseParser:
    def __init__(self, source: StringSource):
        if not isinstance(source, StringSource):
            raise TypeError("Expected `StringSource`, but got: ", type(source))
        self.__source = source

    def _peek(self) -> str:
        if self._is_end():
            raise ValueError("Unexpected end of input")
        return self.__source.peek()
    
    def _take(self) -> str:
        ch = self._peek()
        self.__source.next()
        return ch
    
    def _expected(self, ch: str) -> bool:
        return ch == self._peek()
        
    def _is_end(self) -> bool:
        return not self.__source.has_next()
    
    def _error(self, msg: str) -> ValueError:
        self.__source.error(msg)


class StringCompressedParser(BaseParser):
    def __init__(self, source: StringSource):
        super().__init__(source)
        self.__last_was_char = False

    def validate(self) -> bool:
        try:
            while not self._is_end():
                self.__skip_literals()

                if self._is_end():
                    return True
                
                self.__parse_bracket_open()
            return True
        except (ValueError, TypeError):
            return False

    def __skip_literals(self):
        while not self._is_end():
            if self._expected('('):
                break
            elif self._expected(')'):
                self._error('misplaced bracket')

            self.__last_was_char = True
            self._take()

    def __parse_number_into_brackets(self):
        if self._expected('0'):
            self._take()
        elif self._peek().isdecimal():
            while not self._is_end() and self._peek().isdecimal():
                self._take()
        else:
            self._error('number')

    def __parse_bracket_close(self):
        if self._is_end():
            raise ValueError('Unclosed bracket')
        elif self._expected(')'):
            self._take()
        else:
            self._error('close bracket')

    def __parse_bracket_open(self):
        if self._expected('('):
            self._take()

            if not self.__last_was_char:
                self._error('element expected before bracket')
            self.__last_was_char = False

            self.__parse_number_into_brackets()

            self.__parse_bracket_close()
    

def is_valid_compressed_string(compressed_string: str) -> bool:
    source = StringSource(compressed_string)
    return StringCompressedParser(source).validate()
