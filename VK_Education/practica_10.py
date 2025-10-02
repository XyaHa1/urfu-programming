d = dict()
for w in input().strip().lower().split():
    d[w] = d.get(w, 0) + 1
r = max(d, key=d.get)
print(r, d[r])