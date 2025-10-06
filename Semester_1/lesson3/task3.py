import random


def __select_figura(figures):
    while True:
        i = input("[>] Введите фигуру: ")
        if i in figures:
            return i
        else:
            print("[W] Неверный ввод. Допустимые значения: камень, ножницы, бумага\n")


def play(figures, rules):
    scores = {'HUMAN': 0, 'COMPUTER': 0}
    while scores['HUMAN'] < 3 and scores['COMPUTER'] < 3:

        figure_human: str = __select_figura(figures)
        figure_computer: str = random.choice(figures)
        print(f"[!] Компьютер выбрал {figure_computer}")

        if figure_human == figure_computer:
            print(f"[<>] Ничья")
        elif rules[figure_human] == figure_computer:
            scores['COMPUTER'] += 1
        else:
            scores['HUMAN'] += 1
        print(f'[:] Счет: компьютер - {scores["COMPUTER"]}, вы - {scores["HUMAN"]}')

    return max(scores.items(), key=lambda x: x[1])


def start():
    figures = ['камень', 'ножницы', 'бумага']
    rules = {'камень': 'бумага', 'ножницы': 'камень', 'бумага': 'ножницы'}

    print('== Камень, Ножницы, Бумага ==')
    print(f'[>] Доступные фигуры: {figures}')
    r = play(figures, rules)
    print(f'[O] Победил {r[0]} с {r[1]} очками')


if __name__ == '__main__':
    start()
