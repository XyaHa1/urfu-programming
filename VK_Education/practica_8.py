result = []
for _ in range(int(input())):
    result.append(max(map(int, input().split())))
print(*sorted(result, reverse=True), sep=';')