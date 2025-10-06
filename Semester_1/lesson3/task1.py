import random


def input_num(promt: str) -> int:
    while True:
        n = input(promt)
        if n.isnumeric():
            return int(n)
        else:
            print("[E] Неправильный ввод!")


def answer(a: int, b: int) -> int:
    while True:
        n = input_num("Введите число: ")
        if n < a:
            print(f'[VE] Число опустилось ниже нижней границы: {a}'
                  f'\n[>] Попробуйте еще раз')
        elif n > b:
            print(f'[VE] Число поднялось выше верхней границы: {b}'
                  f'\n[>] Попробуйте еще раз')
        else:
            return n


def game(a: int, b: int):
    n = random.randint(a, b)
    attempt = 0
    while attempt != 3:
        ans = answer(a, b)
        if ans < n:
            print("[!] Загаданное число больше")
            attempt += 1
        elif ans > n:
            print("[!] Загаданное число меньше")
            attempt += 1
        else:
            print("[W] Вы угадали")
            break

        if attempt == 2:
            print(f"[!] Загаданное число: {n % 2 == 0 and 'четное' or 'нечетное'}")

    if attempt == 3:
        print('[L] Вы проиграли. Загаданное число:', n)


def main():
    a = input_num("[>] Введите нижнюю границу диапазона: ")
    b = input_num("[>] Введите верхнюю границу диапазона: ")
    game(a, b)


if __name__ == '__main__':
    main()
