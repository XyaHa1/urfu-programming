print(*map(lambda x: x ** 2 if x % 2 else -x, range(*map(int, input().split()))), sep='\n')
