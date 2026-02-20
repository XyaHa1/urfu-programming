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

    def __peek(self) -> str:
        if self._is_end():
            raise ValueError("Unexpected end of input")
        return self.__source.peek()
    
    def _take(self) -> str:
        ch = self.__peek()
        self.__source.next()
        return ch
    
    def _expected(self, ch: str) -> bool:
        return ch == self.__peek()
    
    def _test(self, filter) -> bool:
        return filter(self.__peek())
        
    def _is_end(self) -> bool:
        return not self.__source.has_next()
    
    def _error(self, msg: str) -> ValueError:
        self.__source.error(msg)


class StringCompressedParser(BaseParser):
    def __init__(self, source: StringSource):
        super().__init__(source)
        self.__can_bracket = False
        self.__last_was_char = False

    def validate(self) -> bool:
        try:
            while not self._is_end():
                self.__skip_literals()
                self.__parse_bracket_open()
            return True
        except (ValueError, TypeError):
            return False

    def __skip_literals(self):

        def is_not_bracket(ch):
            if ch == '(':
                return False
            elif ch == ')':
                self._error('open bracket')
            return True
        
        while not self._is_end():
            if not self._test(is_not_bracket):
                break

            self.__last_was_char = True
            self._take()

    def __parse_number_into_brackets(self):
        if self._expected('0'):
            self._take()
            self.__parse_bracket_close()

        elif self._test(str.isdecimal):
            while not self._is_end() and self._test(str.isdecimal):
                    self._take()
            self.__parse_bracket_close()

        else:
            self._error('number')

    def __parse_bracket_close(self):
        if self._is_end():
            raise ValueError('Unclosed bracket')
        
        elif self._expected(')'):
            self._take()
            self.__can_bracket = False

        else:
            self._error('close bracket')

    def __parse_bracket_open(self):
        if not self._is_end() and self._expected('('):

            if not self.__last_was_char:
                self._error('element expected before bracket')

            self.__last_was_char = False

            self._take()

            if self.__can_bracket:
                self._error('no bracket')

            self.__can_bracket = True
            self.__parse_number_into_brackets()
    

def is_valid_compressed_string(compressed_string: str) -> bool:
    source = StringSource(compressed_string)
    return StringCompressedParser(source).validate()


import unittest

class TestBrokenCases(unittest.TestCase):

    def test_leading_zero_fail(self):
        self.assertFalse(is_valid_compressed_string("a(05)b"), "Ошибка: Ведущий ноль (05) должен быть запрещен")

    def test_double_zero_fail(self):
        self.assertFalse(is_valid_compressed_string("a(00)b"), "Ошибка: Двойной ноль (00) должен быть запрещен")

    def test_zero_with_many_digits_fail(self):
        self.assertFalse(is_valid_compressed_string("a(0123)b"), "Ошибка: Ноль в начале длинного числа должен быть запрещен")

    def test_missing_closing_bracket_fail(self):
        self.assertFalse(is_valid_compressed_string("a(3"), "Ошибка: Отсутствие закрывающей скобки должно вызывать ошибку")

    def test_missing_closing_bracket_after_zero_fail(self):
        self.assertFalse(is_valid_compressed_string("a(0"), "Ошибка: Отсутствие закрывающей скобки после нуля должно вызывать ошибку")

    def test_nested_brackets_complex_fail(self):
        self.assertFalse(is_valid_compressed_string("a(2(3))b"), "Ошибка: Вложенные скобки должны быть запрещены")

    def test_only_open_bracket_fail(self):
        self.assertFalse(is_valid_compressed_string("a("), "Ошибка: Одинокая открывающая скобка должна вызывать ошибку")

    def test_text_inside_brackets_fail(self):
        self.assertFalse(is_valid_compressed_string("a(b)c"), "Ошибка: Буквы внутри скобок запрещены")

    def test_space_inside_brackets_fail(self):
        self.assertFalse(is_valid_compressed_string("a( 3 )b"), "Ошибка: Пробелы внутри скобок с числом недопустимы")

    def test_edges_cases(self):
        self.assertTrue(is_valid_compressed_string(""))
        self.assertFalse(is_valid_compressed_string("()"))
        self.assertTrue(is_valid_compressed_string("a(1)"))
    
    def test_long_strings(self):
        self.assertTrue(is_valid_compressed_string("a" * 1000 + "(1000)" + "b" * 1000))

    def test_special_characters(self):
        self.assertTrue(is_valid_compressed_string("a(1)@b(2)"))
        self.assertTrue(is_valid_compressed_string("a(1)b(0)c(3)"))

    def test_valid_strings(self):
        valid_strings = [
            "a(3)b(2)c",
            "a(1)b(2)c(3)",
            "a(123)b(45)c(6)",
            "a(1)b(9)c(3)",
            "abc",
            "1(1)",
            "",
            "a(1)b(0)c(3)"
        ]
        for s in valid_strings:
            with self.subTest(s=s):
                self.assertTrue(is_valid_compressed_string(s))
    
    def test_edge_cases(self):
        self.assertTrue(is_valid_compressed_string(""))
        self.assertFalse(is_valid_compressed_string("()"))
        self.assertTrue(is_valid_compressed_string("a(1)"))
        self.assertFalse(is_valid_compressed_string("(1)"))
        self.assertFalse(is_valid_compressed_string("a(1)2(b"))

    
    def test_invalid_strings(self):
        invalid_strings = [
            "a(3))b((2)c",
            "a(03)b",
            "a((3))b",
            "a(b(2)c)d(3)",
            "()",
            "a(1)(2)b",
            "a(1)b)(",
            "a(1)b()",
            "(1)a",
            "a(1)2(b",
            "s@@09(287j)",
            "a(1))b",
            "a(1)b)"
        ]
        for s in invalid_strings:
            with self.subTest(s=s):
                self.assertFalse(is_valid_compressed_string(s))

if __name__ == '__main__':
    unittest.main()
