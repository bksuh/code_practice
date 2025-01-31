C, K, P = map(int, input().split())

ans = 0
for i in range(1, C+1):
    ans += (K*i + P*pow(i, 2))
print(ans)