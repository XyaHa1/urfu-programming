s = input().strip().split()
print(round(sum(map(len, s)) / len(s), 2) if s else 0.00)