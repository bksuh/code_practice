grid = [[0]*101 for _ in range(101)]
cnt = 0
for _ in range(4):
    a, b, c , d = map(int, input().split())
    for i in range(a, c):
        for j in range(b, d):
            if grid[i][j] == 0:
                cnt+=1
                grid[i][j] = 1
            else:
                continue
print(cnt)