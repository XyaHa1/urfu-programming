i = f'{int(input()):0=+10}'
f = float(input())
if f >= 0:
    f = f'{f:#=10.2f}'
elif f < 0:
    f = f'{f:#>+10.2f}'

b = f'{int(input()):016b}'

print(i, f, sep='\n')

for i in range(16):
    if i % 4 == 0 and i != 0:
        print('_', end='')
    print(b[i], end='')