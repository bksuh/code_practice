n=int(input())
drinks=[int(input()) for _ in range(n)]

dp=[0]*10000
dp[0]=drinks[0]
if len(drinks) >= 2:
    dp[1]=drinks[0]+drinks[1]
if len(drinks) >= 3:
    dp[2]=max(drinks[2]+drinks[0], drinks[2]+drinks[1], dp[1])
for i in range(3,n):
  dp[i]=max(drinks[i]+dp[i-2], drinks[i]+drinks[i-1]+dp[i-3], dp[i-1])

print(max(dp))