numerator, denominator = int(input()), int(input())


def changed_div(numerator, denominator):
    try:
        a = numerator / denominator
        return denominator / a
    except ZeroDivisionError:
        return denominator


print(changed_div(numerator, denominator))
