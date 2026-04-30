from task3 import is_valid_compressed_string

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
        self.assertFalse(is_valid_compressed_string("abs("))
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
