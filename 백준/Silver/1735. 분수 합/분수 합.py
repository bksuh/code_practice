from math import gcd

a, b = map(int, input().split())
c, d = map(int, input().split())

x = a*d + c*b
y = b*d

tmp = gcd(x, y)
print(f"{x//tmp} {y//tmp}")