def print_pack_report(count: int) -> None:
    if count < 1:
        print("No packages to send")
        return

    for i in range(count, 0, -1):
        if i % 3 == 0 and i % 5 == 0:
            print(f"{i} - расфасуем по 3 или по 5")
        elif i % 3 == 0:
            print(f"{i} - расфасуем по 3")
        elif i % 5 == 0:
            print(f"{i} - расфасуем по 5")
        else:
            print(f"{i} - не заказываем!")


if __name__ == "__main__":
    count = int(input("Введите количество пирожных: "))
    print_pack_report(count)