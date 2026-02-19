def compress_string(original_string: str) -> str:
    if not isinstance(original_string, str):
        raise ValueError(f"Expected string, got {type(original_string).__name__}")

    if not original_string:
        return ""

    result = []
    frequency = 0
    i = 0
    while i < len(original_string):
        ch = original_string[i]

        if ch in "()":
            result.append(ch)
            i += 1
            continue

        while i < len(original_string) and original_string[i] == ch:
            frequency += 1
            i += 1
        result.append(f'{ch}{f"({frequency})" if frequency > 1 else ""}')
        frequency = 0

    return "".join(result)


def decompress_string(compressed_string: str) -> str:
    if not isinstance(compressed_string, str):
        raise ValueError(f"Expected string, got {type(compressed_string).__name__}")

    if not compressed_string:
        return ""

    result = []
    i = 0
    curr_ch = ""
    mult = 1
    while i < len(compressed_string):
        if compressed_string[i] in "(":
            start = i
            while i < len(compressed_string) and compressed_string[i] != ")":
                i += 1

            if i < len(compressed_string):
                i += 1

            seq = compressed_string[start:i]
            if seq[1:-1].isdigit():
                mult = int(seq[1:-1])
                result[-1] = result[-1] * mult if mult > 1 and result else []
            else:
                result.append(seq)
        else:
            curr_ch = compressed_string[i]
            i += 1
            result.append(curr_ch)

    return "".join(result)
