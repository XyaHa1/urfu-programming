import random
import string


def generate_password(length: int,
                      use_uppercase: bool,
                      use_lowercase: bool,
                      use_digits: bool,
                      use_symbols: bool,
                      ) -> str:
    """
    Генерирует пароль заданной длины с использованием указанных символов.
    """
    character_set = []
    password = []
    if use_uppercase:
        password.append(random.choice(string.ascii_uppercase))
        character_set += string.ascii_uppercase
    if use_lowercase:
        password.append(random.choice(string.ascii_lowercase))
        character_set += string.ascii_lowercase
    if use_digits:
        password.append(random.choice(string.digits))
        character_set += string.digits
    if use_symbols:
        password.append(random.choice(string.punctuation))
        character_set += string.punctuation

    password += [random.choice(random.choice(character_set)) for _ in range(length - len(password))]
    random.shuffle(password)

    return ''.join(password)


def ask(question: str) -> bool:
    while True:
        r = input(question).lower()
        if r == 'y':
            return True
        elif r == 'n':
            return False
        else:
            print(
                "[!] Неверный ответ. Пожалуйста, введите 'y' для подтверждения или 'n' для отмены.")


def ask_length(min_length=8) -> int:
    while True:
        if (n := input(f"[!] Введите длину пароля (Минимальная длина: {min_length}): ")).isdigit():
            n = int(n)
            if n < min_length:
                print(f"[!] Минимальная длина пароля: {min_length}.")
            else:
                return n
        else:
            print("[!] Неверный ответ. Пожалуйста, введите число.")


def main():
    """
    Основная функция программы.
    """

    print("Генератор сложных паролей.")
    length = ask_length()
    count_true = 0

    flag_upper: bool
    flag_lower: bool
    flag_digits: bool
    flag_symbols: bool

    while count_true < 2:
        flag_upper = ask("[!] Использовать заглавные буквы? (y/n): ")
        if flag_upper:
            count_true += 1
        flag_lower = ask("[!] Использовать строчные буквы? (y/n): ")
        if flag_lower:
            count_true += 1
        flag_digits = ask("[!] Использовать цифры? (y/n): ")
        if flag_digits:
            count_true += 1
        flag_symbols = ask("[!] Использовать спецсимволы? (y/n): ")
        if flag_symbols:
            count_true += 1
        if count_true < 2:
            print('[>] Необходимо выбрать хотя бы два типа символов.')


    password = generate_password(length, flag_upper, flag_lower, flag_digits, flag_symbols)

    print("Сгенерированный пароль:", password)


if __name__ == "__main__":
    main()
