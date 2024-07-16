n, t = map(int, input().split())
paper = [list(map(int, input().split())) for _ in range(n)]

grid = [[0]*101 for _ in range(101)]

for x,y,a,b in paper:
    for i in range(x, a+1):
        for j in range(y, b+1):
            grid[i][j] +=1
sum = 0
for i in range(101):
    for j in range(101):
        if grid[i][j] > t:
            sum+=1

print(sum)
