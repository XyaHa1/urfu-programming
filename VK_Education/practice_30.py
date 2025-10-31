class Dictionary:
    def __init__(self, dictionary):
        self._dict = dictionary

    def __call__(self, key):
        return self._dict.get(key, None)


code = []
while data := input():
    code.append(data)
code = "\n".join(code)
exec(code)
