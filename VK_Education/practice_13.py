def func(s: str):
    normal_s = s.upper() if s[0] == '!' else s.lower()
    return (normal_s
            .replace('!', '')
            .replace('@', '')
            .replace('#', '')
            .replace('%', ''))


while (s := input()) != '':
    print(func(s))
