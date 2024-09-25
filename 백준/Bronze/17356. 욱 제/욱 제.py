a, b = map(int, input().split())
m = (b-a)/400
tmp = pow(10, m)
ans = 1/(1+tmp)

print(ans)