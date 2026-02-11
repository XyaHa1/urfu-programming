from math import gcd


def f_2_5(q: int):
    """
    Любое десятичное число можно разложить на q = (2 ** a) * (5 ** b) * m
    """
    p2, p5, m = 0, 0, 0
    while q != 0:
        if q % 2 == 0:
            p2 += 1
            q //= 2
        elif q % 5 == 0:
            p5 += 1
            q //= 5
        else:
            m = q
            q = 0

    return p2, p5, m

def search_pre_T(n: int, d: int, length: int) -> tuple[str, int]:
    res = []
    
    for _ in range(length):
        n *= 10
        res.append(str(n // d))
        n %= d
        if n == 0:
            break

    return "".join(res), n

def search_T(m: int, n: int, d: int) -> str:
    if m == 1:
        return ""

    res = ['(']
    rem = {}
    n *= 10
    digit = str(n // d)
    rem[n // 10] = digit
    res.append(digit)
    n %= d

    while True:
        r = n
        n *= 10
        digit = str(n // d)
        n %= d
        if n in rem:
            break
        rem[r] = digit
        res.append(digit)
    
    res.append(")")

    return ''.join(res)


def rational_to_decimal(num: int, den: int, prec: int = 10) -> str:

    if not all((isinstance(num, int), isinstance(den, int), isinstance(prec, int))):
        raise ValueError()

    if den == 0:
        raise ValueError()

    k = gcd(num, den)
    """
    Если НОК(числителя, знаменателя) = знаменателю, то
        знаминатель делит числитель нацело.
    """
    if k == abs(den):
        return str(num // den)

    sign = (-1) ** ((num > 0) + (den < 0) + 1)
    num, den = abs(num) // k, abs(den) // k

    left = num // den
    n2, n5, m = f_2_5(den)
    length_pre_T = max(n2, n5)

    pre_T, n = search_pre_T(num % den, den, length_pre_T)
    T = search_T(m, n, den)

    right = f"{pre_T}{T}"
    if len(right) > prec:
        right = right[:prec + 1]
        li = right.rfind('(')
        ri = right.rfind(')')
        if li != -1 and ri == -1:
            right = f"{right[:li]}{right[li + 1:]}"

    
    res = ""
    if sign < 0:
        res += "-"
    res += f"{left}.{right}"

    return res

print(rational_to_decimal([], 1))