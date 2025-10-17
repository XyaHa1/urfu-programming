from fridge_system import Fridge


def select_option():
    while True:
        try:
            option = int(input("Введите номер операции: "))
            if option in range(1, 11):
                return option
            else:
                print("[WARNING] Неверный номер операции. Попробуйте еще раз.")
        except ValueError:
            print("[ERROR] Неверный ввод. Попробуйте еще раз.")


def ask(prompt: str):
    return input(prompt)


def help_input_items(flag):
    if flag:
        print('[!] Пример ввода: "<название>, <количество>, <дата>"\n'
              '                  "<название>, <количество>"\n'
              '[!] Формат даты: "ГГГГ-ММ-ДД"\n'
              '[!] Например: "яблоки, 2, 2023-04-20"')


def help_search_items(flag):
    if flag:
        print('[!] Пример вводы: "<слово1>", "<слово2>", ...\n"'
              '                  "<слово1>"\n'
              '[!] Перечисление слов через запятую')


def main():
    fridge = Fridge({})
    print("Добро пожаловать в систему хранения продуктов!\n")
    print("======== MENU ========\n"
          "1. Добавить продукт\n"
          "2. Поиск продуктов по ключевым словам\n"
          "3. Количество продуктов по ключевым словам\n"
          "---\n"
          "4. Отключить подсказки\n"
          "5. Включить подсказки\n"
          "---\n"
          "0. Выход\n")
    help = True
    while True:
        option = select_option()
        match option:
            case 1:
                help_input_items(help)
                fridge.add_by_note(ask("[>] Введите данные продукта: "))
            case 2:
                help_search_items(help)
                print(fridge.find(ask("[>] Введите ключевые слова: ")))
            case 3:
                help_search_items(help)
                print(fridge.amount(ask("[>] Введите ключевые слова: ")))
            case 4:
                if help:
                    help = False
                    print("[INFO] Подсказки отключены")
                else:
                    print("[INFO] Подсказки включены")
            case 5:
                if help:
                    print("[INFO] Подсказки включены")
                else:
                    help = True
                    print("[INFO] Подсказки отключены")
            case 0:
                print("До свидания!")
                exit(0)


if __name__ == '__main__':
    main()
