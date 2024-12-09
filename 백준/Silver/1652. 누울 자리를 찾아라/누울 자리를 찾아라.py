n = int(input())
grid = [input() for _ in range(n)]

ver, hor = 0, 0
for i in range(n):
    tmp = grid[i].split('X')
    for ans in tmp:
        if ans == '' or ans == '.':
            continue
        else:
            ver += 1

for j in range(n):
    ans = ''
    for k in range(n):
        ans += grid[k][j]
    tmp = ans.split('X')
    for ans in tmp:
        if ans == '' or ans == '.':
            continue
        else:
            hor += 1

print(ver, hor)