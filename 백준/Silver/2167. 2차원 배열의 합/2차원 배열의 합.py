n, m = map(int, input().split())
grid = []
for _ in range(n):
    tmp = list(map(int, input().split()))
    grid.append(tmp)

dp = [[0]*(m+1) for _ in range(n+1)] 

for i in range(1, n+1):
    for j in range(1, m+1):
        dp[i][j] = grid[i-1][j-1] + dp[i-1][j] + dp[i][j-1] - dp[i-1][j-1]

        
t = int(input())
for _ in range(t):
    i, j, x, y = map(int, input().split())
    print(dp[x][y] - dp[i-1][y] - dp[x][j-1] + dp[i-1][j-1]) 