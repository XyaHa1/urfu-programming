from typing import List


def encryption_dict(shift: int, arr_chars: List[str]) -> dict:
    return {arr_chars[i]: arr_chars[(i + shift) % len(arr_chars)] for i in range(len(arr_chars))}


def decryption_dict(shift: int, arr_chars: List[str]) -> dict:
    return {arr_chars[i]: arr_chars[(i - shift) % len(arr_chars)] for i in range(len(arr_chars))}


def auto_lang(text: str) -> str:
    return 'eng' if text.isascii() else 'ru'


def cabinet_caesar(text: str, shift: int, encrypt: bool) -> str:
    text = text.lower()
    lang = auto_lang(text)
    lang_dict = {'ru': [chr(i) for i in range(ord('а'), ord('я') + 1)],
                 'eng': [chr(i) for i in range(ord('a'), ord('z') + 1)]}
    arr_chars = lang_dict[lang]
    arr_shift: dict
    if encrypt:
        arr_shift = encryption_dict(shift, arr_chars)
    else:
        arr_shift = decryption_dict(shift, arr_chars)

    return ''.join([arr_shift.get(ch, ch) for ch in text])


if __name__ == '__main__':
    print("========================\n"
          "       Шифр Цезаря      \n"
          "========================\n"
          )
    text: str = input("[!] Введите текст: ")
    flag_encrypt = input("[!] Введите 1 для шифрования, 0 для дешифрования: ")

    if flag_encrypt == '1':
        flag_encrypt = True
    elif flag_encrypt == '0':
        flag_encrypt = False
    else:
        print("[!] Неверный ввод")
        exit(0)

    count_shift = int(input("[!] Введите сдвиг: "))

    new_text = cabinet_caesar(text, count_shift, flag_encrypt)
    print("[!] Результат: ", new_text, "\n")