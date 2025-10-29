memory = {1: 1, 2: 1}


def fibbonacci(n):
    if n in memory:
        return memory.get(n)
    memory[n] = fibbonacci(n - 1) + fibbonacci(n - 2)
    return memory.get(n)


print(fibbonacci(int(input())))
