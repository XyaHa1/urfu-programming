import datetime

days, seconds = int(input()), int(input())


def shift_time(days: int, seconds: int):
    base = datetime.datetime(2023, 1, 1, 12, 30, 0)
    shifted = base + datetime.timedelta(days=days, seconds=seconds)
    return (shifted.day, shifted.second)


print(shift_time(days, seconds))
