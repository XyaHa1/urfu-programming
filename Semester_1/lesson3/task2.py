import string
from typing import Set, Dict, Tuple


def select_sets_of_lang(lang: str) -> Tuple[Set[str], Set[str]]:
    vowels: Set[str] = set()
    cons: Set[str] = set()

    if 'ru' in lang:
        vowels.update({'а', 'о', 'и', 'е', 'ё', 'э', 'ы', 'у', 'ю', 'я'})
        cons.update({'б', 'в', 'г', 'д', 'ж', 'з', 'й', 'к', 'л', 'м', 'н',
                'п', 'р', 'с', 'т', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ь'})
    if 'eng' in lang:
        vowels.update({'a', 'e', 'i', 'o', 'u', 'y'})
        cons.update({'b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm',
                'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'z',})

    return vowels, cons


def analys(text: str, lang: str):
    vowels, cons = select_sets_of_lang(lang)

    result: Dict = {
        "vowels": 0,
        "cons": 0,
        "whitespace": 0,
        "top_3_frequent_symbols": [],
        "count_words": 0,
    }

    all_chars: Dict[str, int] = {}
    i = 0
    while i < len(text):
        ch = text[i].lower()

        if ch.isspace():
            result['whitespace'] += 1
            i += 1

        elif ch in string.punctuation:
            all_chars[ch] = all_chars.get(ch, 0) + 1
            i += 1

        elif ch.isalnum():
            while i < len(text) and text[i].isalnum() and not text[i].isspace():
                ch = text[i].lower()

                if ch in vowels or ch in cons:
                    if ch in vowels:
                        result['vowels'] += 1
                    elif ch in cons:
                        result['cons'] += 1

                ch = text[i]
                all_chars[ch] = all_chars.get(ch, 0) + 1
                i += 1

            result['count_words'] += 1

        else:
            i += 1

    result['top_3_frequent_symbols'] = sorted(all_chars.items(), key=lambda x: x[1], reverse=True)[:3]

    return result


def select_lang():
    while True:
        l = input("[>] Провести анализ текста на основе (ru, eng, ru/eng): ")
        if l == 'ru' or l == 'eng' or l == 'ru/eng':
            return l
        else:
            print("[W] Неверный язык. Введите 'ru', 'eng' или 'ru/eng'")


def start():
    lang = select_lang()
    text = input("[>] Введите текст: ")

    res = analys(text, lang)

    vowels = res['vowels']
    cons = res['cons']
    whitespace = res['whitespace']
    top_3 = res['top_3_frequent_symbols']
    count_words = res['count_words']

    print(f"\n[O] Результат анализа на основе "
          f"{'русского' if lang == 'ru' else 'английского' 
          if lang == 'eng' else 'русского и английского'} набора: \n"
          f"    Гласных букв: {vowels}\n"
          f"    Согласных букв: {cons}\n"
          f"[O] Общие данные: \n"
          f"    Топ-3 символа: {top_3}\n"
          f"    Количество слов: {count_words}\n"
          f"    Пробелов: {whitespace}\n")


if __name__ == '__main__':
    start()
