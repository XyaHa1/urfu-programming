d = dict()
i = 0
string = input()
while i < len(string):
    start = i
    while i < len(string) and string[i].isalpha():
        i += 1
    if i > start and i - start >= 5:
        w = string[start:i].lower()
        if len(set(w)) >= 4:
            d[w] = d.get(w, 0) + 1
    i += 1

sorted_d = sorted(filter(lambda key: d.get(key) > 2, d))
print(*sorted_d, sep='\n')
