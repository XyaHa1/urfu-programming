def repeat_deco(n=1):
    def deco(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            for _ in range(n - 1):
                result = func(*args, **kwargs)
            return result

        return wrapper

    return deco


code = []
while data := input():
    code.append(data)
code = "\n".join(code)
exec(code)
