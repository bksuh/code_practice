n, m = map(int, input().split())
check = []
for i in range(n):
    tmp = list(map(int, input().split()))
    for j in range(m):
        if tmp[j] == 1:
            check.append((i,j))

x1, y1 = check[0]
x2, y2 = check[1]

print(abs(x1 - x2) + abs(y1 - y2))