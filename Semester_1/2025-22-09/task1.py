def parity(n: int) -> bool:
    return n % 2 == 0


def sign(n: int) -> None | bool:
    if n == 0:
        return None
    return n > 0


def interval(n: int) -> bool:
    return 10 <= n <= 50


def main():
    n = int(input())

    p = parity(n)
    s = sign(n)
    i = interval(n)

    result = dict()
    result["parity"] = "parity" if p else "not parity"
    result["sign"] = "positive" if s else "negative" if s is False else "zero"
    result["interval"] = "in" if i else "out"
    print(result)


if __name__ == "__main__":
    main()
