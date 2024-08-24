dp = [-1 for i in range(100001)]
dp[2] = 1
dp[4] = 2
dp[5] = 1
n = int(input())
for i in range(6, n+1):
    a, b = dp[i-2], dp[i-5]
    if a == -1 and b != -1:
        dp[i] = dp[i-5] + 1
    elif a != -1 and b == -1:
        dp[i] = dp[i-2] + 1
    elif a== -1 and b== -1:
        continue
    else:
        dp[i] = min(dp[i-2] + 1, dp[i-5] + 1)
print(dp[n])