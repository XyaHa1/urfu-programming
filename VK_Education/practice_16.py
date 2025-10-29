def map(func, seq):
    for x in seq:
        yield func(x)


func_in, seq_in = eval(input()), eval(input())

for x in map(func_in, seq_in):
    print(x)
