from math import log10, floor


def func(n: int):
    all_length = 0 # длина всех чисел
    for i in range(1, 2 ** 31 - 1):
        all_length += floor(log10(i) + 1) # вычисляем длину числа
        if n < all_length:
            ind = all_length - n
            num = str(i)[-ind]
            return num


if __name__ == '__main__':
    while True:
        ind = int(input('[>] Введите индекс символа: '))
        print(func(ind))
