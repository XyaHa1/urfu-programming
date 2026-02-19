def custom_string_to_int(string_representation: str) -> int:
    if not isinstance(string_representation, str):
        raise ValueError()

    string_representation = string_representation.strip()
    if not string_representation:
        raise ValueError()

    flag = string_representation[0] == "-"
    sign = 1
    if flag:
        string_representation = string_representation[1:]
        sign = -1

    if not string_representation:
        raise ValueError()

    result = 0
    i = 0
    while i < len(string_representation):
        d = ord(string_representation[i]) - ord("0")

        if d > 9 or d < 0:
            raise ValueError()

        result = result * 10 + d
        i += 1

    return sign * result
