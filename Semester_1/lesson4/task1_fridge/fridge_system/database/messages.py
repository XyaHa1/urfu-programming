from enum import Enum


class Messages(Enum):
    FILE_NOT_FOUND = "[WARNING] Файл не найден: {}"
    INVALID_FORMAT_FILE = "[WARNING] Файл не соответствует формату (.csv, .json): {}"
    TITLE_NOT_FOUND = "[WARNING] Не найден заголовок продукта: {}"
    INVALID_INDEX = "[WARNING] Индекс выходит за границы списка: {}"
