n = int(input())

for _ in range(n):
    h, w = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(h)]
    ans = []
    for i in range(w):
        tmp = []
        for j in range(h):
            tmp.append(grid[j][i])
        ans.append(tmp)
    real = 0
    for i in range(len(ans)):
        for j in range(len(ans[i])):
            if ans[i][j] == 1:
                real += ans[i][j+1::].count(0)
    print(real)