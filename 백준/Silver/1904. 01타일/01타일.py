n = int(input())

dp = [0, 1, 2]
for _ in range(3, n+1):
    dp.append((dp[-1]+dp[-2])%15746)
print(dp[n])