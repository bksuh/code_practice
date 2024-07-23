import math
a, b = map(int, input().split(':'))
tmp = math.gcd(a, b)
print(f"{a//tmp}:{b//tmp}")