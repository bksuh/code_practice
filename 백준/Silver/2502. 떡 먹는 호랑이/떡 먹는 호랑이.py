n, tar = map(int, input().split())
dp = [[0, 0] for _ in range(31)]
dp[1] = [1, 0]
dp[2] = [0, 1]
for i in range(3, n+1):
    dp[i] = [dp[i-1][1], dp[i-1][0]+dp[i-1][1]]
a, b = dp[n]
ans1, ans2 = 1, 0
while True:
    ans2 = (tar - a*ans1)//b
    if a*ans1 + b*ans2 == tar and (tar-a*ans1)%b == 0:
        print(ans1)
        print(ans2)
        break
    ans1+=1

