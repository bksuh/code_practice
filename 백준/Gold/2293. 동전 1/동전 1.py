n, k = map(int, input().strip().split())
arr = [int(input()) for _  in range(n)]

dp = [0 for i in range(k + 1)]
dp[0] = 1

for coin in arr:
    for i in range(coin, k + 1):
        dp[i] += dp[i - coin]

print(dp[k])