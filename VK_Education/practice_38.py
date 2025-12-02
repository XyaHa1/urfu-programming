import datetime

string_datetime = input()


def parse_time(s):
    dt = datetime.datetime.strptime(s, "%Y %m %d %H %M %S")
    dt_shifted = dt + datetime.timedelta(days=1)
    return dt_shifted.day


print(parse_time(string_datetime))
