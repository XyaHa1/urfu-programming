import string


def check_letter(ch: str, s: set) -> int:
    if ch in s:
        return 1
    return 0


def check_symbol(ch: str, vowels: set, cons: set) -> bool:
    return ch in vowels or ch in cons or ch in string.digits


def analys(text: str, lang: str):
    vowels: set
    cons: set

    if lang == 'ru':
        vowels = {'а', 'о', 'и', 'е', 'ё', 'э', 'ы', 'у', 'ю', 'я'}
        cons = {'б', 'в', 'г', 'д', 'ж', 'з', 'й', 'к', 'л', 'м', 'н', 'п', 'р', 'с', 'т', 'ф', 'х', 'ц', 'ч', 'ш',}
    elif lang == 'eng':
        vowels = {'a', 'e', 'i', 'o', 'u', 'y'}
        cons = {'b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'z',}

    result: dict = {
        "vowels": 0,
        "cons": 0,
        "whitespace": 0,
        "frequent symbols (top-3)": [],
        "count_words": 0,
    }

    letters = {}
    i = 0
    while i < len(text):
        ch = text[i].lower()
        if ch.isspace():
            result['whitespace'] += check_letter(ch, string.whitespace)
        elif ch not in string.punctuation:
            while i < len(text) and check_symbol(text[i].lower(), vowels, cons):
                ch = text[i].lower()
                result['vowels'] += check_letter(ch, vowels)
                result['cons'] += check_letter(ch, cons)
                letters[ch] = letters.get(ch, 0) + 1
                i += 1

            result['count_words'] += 1
        i += 1

    result['frequent symbols (top-3)'] = sorted(letters.items(), key=lambda x: x[1], reverse=True)[:3]

    return result


def ans_lang():
    while True:
        l = input("[>] Введите язык текста (ru/eng): ")
        if l == 'ru' or l == 'eng':
            return l
        else:
            print("[W] Неверный язык. Введите 'ru' или 'eng'")


def main():
    lang = ans_lang()
    text = input("[>] Введите текст: ")
    res = analys(text, lang)
    print(res, sep='\n')


if __name__ == '__main__':
    # assert analys("Живи так, как будто будешь жить вечно, и ты будешь жить для всех. ", 'ru') == {'vowels': 18,
    #                                                                'cons': 42,
    #                                                                'whitespace': 13,
    #                                                                'frequent words (top-3)': [('жиnm', 2), ('будто', 2), ('будешь', 2)],
    #                                                                'count_words': 13}
    print(analys("Живи так, как будто будешь жить вечно, и ты будешь жить для всех. ", 'ru'))




