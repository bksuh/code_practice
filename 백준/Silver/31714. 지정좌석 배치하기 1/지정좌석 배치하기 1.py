n, m, d = map(int, input().split())

grid = []
for i in range(1, n+1):
    tmp = list(map(int, input().split()))
    for j in range(len(tmp)):
        tmp[j] = tmp[j] + (d*i)
    tmp.sort()
    grid.append(tmp)
indi = True
for j in range(m):
    for i in range(1, n):
        if grid[i-1][j] >= grid[i][j]:
            indi = False
            break
    if not indi:
        break

print("YES" if indi else "NO")