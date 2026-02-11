def custom_string_to_int(string: str) -> int:
    if not isinstance(string, str):
        raise ValueError()

    string = string.strip()
    if not string:
        raise ValueError()

    flag = string[0] == "-"
    sign = 1
    if flag:
        string = string[1:]
        sign = -1

    if not string:
        raise ValueError()

    result = 0
    i = 0
    while i < len(string):
        d = ord(string[i]) - ord("0")

        if d > 9 or d < 0:
            raise ValueError()

        result = result * 10 + d
        i += 1

    return sign * result
