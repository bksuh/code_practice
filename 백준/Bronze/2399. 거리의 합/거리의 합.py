import sys
input = sys.stdin.readline

n = int(input())
x = list(map(int, input().split()))

x.sort()
dp = [0] * (n + 1)
sum = 0
for i in range(1, n):
    dp[i] = dp[i - 1] + (x[i] - x[i - 1]) * i
    sum += dp[i]
print(sum * 2)