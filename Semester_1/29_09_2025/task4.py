import random
import string


def generate_password(length: int,
                      use_uppercase: bool,
                      use_lowercase: bool,
                      use_digits: bool,
                      use_symbols: bool) -> str:
    """
    Генерирует пароль заданной длины с использованием указанных символов.
    """

    character_set = ''
    if use_uppercase:
        character_set += string.ascii_uppercase
    if use_lowercase:
        character_set += string.ascii_lowercase
    if use_digits:
        character_set += string.digits
    if use_symbols:
        character_set += string.punctuation

    password = ''.join(random.choice(character_set) for _ in range(length))

    return password


def main():
    """
    Основная функция программы.
    """

    print("Генератор сложных паролей.")
    length = int(input("[!] Введите длину пароля: "))
    flag_upper = input("[!] Использовать заглавные буквы? (y/n): ").lower() == 'y'
    flag_lower = input("[!] Использовать строчные буквы? (y/n): ").lower() == 'y'
    flag_digits = input("[!] Использовать цифры? (y/n): ").lower() == 'y'
    flag_symbols = input("[!] Использовать спецсимволы? (y/n): ").lower() == 'y'

    password = generate_password(length, flag_upper, flag_lower, flag_digits, flag_symbols)

    print("Сгенерированный пароль:", password)


if __name__ == "__main__":
    main()
