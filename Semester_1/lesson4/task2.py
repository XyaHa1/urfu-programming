def correct_brackets(exp: str):
    brackets = 0
    for ch in exp:
        if ch == "(":
            brackets += 1
        elif ch == ")":
            brackets -= 1
        if brackets < 0:
            return False

    return brackets == 0


def test():
    assert correct_brackets("(())") is True
    assert correct_brackets("((()))") is True
    assert correct_brackets("()") is True
    assert correct_brackets("((2+2)2)") is True
    assert correct_brackets("((2+2)2)(") is False
    assert correct_brackets("((2+2)2))(") is False
    assert correct_brackets(")(") is False
    assert correct_brackets("") is True
    assert correct_brackets(")") is False
    assert correct_brackets("(") is False


if __name__ == "__main__":
    test()
    while True:
        exp = input("[>] Введите выражение: ")
        print(f"[!] Правильность скобок: {correct_brackets(exp)}")
