def cache_deco(func):
    cache = dict()

    def wrapper(*args):
        if args in cache:
            return cache[args]
        cache[args] = func(*args)
        return cache[args]

    return wrapper


code = []
while data := input():
    code.append(data)
code = "\n".join(code)
exec(code)
