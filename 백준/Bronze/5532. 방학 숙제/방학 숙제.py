import math

a = int(input())
m = int(input())
k = int(input())
m1 = int(input())
k1 = int(input())

tmp1 = math.ceil(m/m1)
tmp2 = math.ceil(k/k1)

print(a - max(tmp1, tmp2))