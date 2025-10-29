def cache_deco(func):
    cache = dict()

    def wrapper(*args):
        if args in cache:
            return cache[args]
        cache[args] = func(*args)
        return cache[args]

    return wrapper


def solution(func_map, func_filter, data):
    filtered_data = map(func_map, filter(func_filter, data))
    for i, v in enumerate(filtered_data):
        if i % 2 == 0:
            yield v


code = []
while data := input():
    code.append(data)
code = "\n".join(code)
exec(code)
