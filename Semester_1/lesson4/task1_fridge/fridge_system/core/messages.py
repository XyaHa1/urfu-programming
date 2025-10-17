from enum import Enum


class Messages(Enum):
    INVALID_CHARS_TITLE = ("[ERROR] Заголовок не должен содержать символы, \n"
                           "кроме латинских и русских букв, пробелов и дефисов: {}")
    INCORRECT_DOT_AMOUNT = "[ERROR] Количество точек не должно быть больше 1: {}"
    INCORRECT_COMMA_AMOUNT = "[ERROR] Запятые не должны содержаться в количестве: {}"
    START_END_DOT_AMOUNT = "[ERROR] Начало и конец количества не должны содержать точку: {}"
    NEGATIVE_AMOUNT = "[ERROR] Количество не может быть отрицательным: {}"
    DECIMAL_AMOUNT = "[ERROR] Не может быть переведено в тип Decimal: {}"
    INCORRECT_FORMAT_DATE = ("[ERROR] Неверный формат даты: {}\n"
                             "[EXPECTED] {}")
    INCORRECT_SEPARATOR = "[ERROR] Неверный разделитель между данными"
    EMPTY_ITEMS = "[WARNING] Данные не были введены"
    INCORRECT_COUNT_ITEMS = "[ERROR] Количество данных не соответствует требованиям: {}"
    EMPTY_ITEM = "[ERROR] Один из элементов пустой"
