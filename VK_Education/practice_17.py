def filter(func, seq):
    for x in seq:
        if func(x):
            yield x


func_in, seq_in = eval(input()), eval(input())

for x in filter(func_in, seq_in):
    print(x)
