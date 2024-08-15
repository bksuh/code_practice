import math
a, b = map(int, input().split())
tmp = math.gcd(a, b)
ans = (a*b)//tmp
print(ans)