class Counter:

    def __init__(self, initial_count):
        self._count = initial_count

    def increment(self):
        self._count += 1

    def get(self):
        return self._count


code = []
while data := input():
    code.append(data)
code = "\n".join(code)
exec(code)
