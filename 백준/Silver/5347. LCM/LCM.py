import math

n = int(input())

for _ in range(n):
    a, b = map(int, input().split())
    tmp = math.gcd(a, b)
    print(abs(a*b)//tmp)