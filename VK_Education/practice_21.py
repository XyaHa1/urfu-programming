def g():
    global b
    b = int(input())

    def h():
        global b
        b += 10

    h()
    print(b)


g()
