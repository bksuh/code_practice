grid = [[0]*3 for _ in range(3)]
t = int(input())
winner = 0
for _ in range(9):
    x, y = map(int, input().split())
    ans = []
    if t%2 == 0:
        grid[x-1][y-1] = 2
    else:
        grid[x-1][y-1] = 1
    t+=1
    for i in range(3):
        ans.append(grid[i])
        ans.append([grid[0][i], grid[1][i], grid[2][i]])
    ans.append([grid[0][0], grid[1][1], grid[2][2]])
    ans.append([grid[2][0], grid[1][1], grid[0][2]])
    if winner == 0 and [1, 1, 1] in ans: 
        winner = 1
    if winner == 0 and [2, 2, 2] in ans:
        winner = 2
print(winner)
