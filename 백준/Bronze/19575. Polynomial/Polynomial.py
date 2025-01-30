import sys

MOD = 1000000007
input = sys.stdin.readline
N, X = map(int, input().split())
coefficients = []
for _ in range(N+1):
    a, b = map(int, input().split())
    coefficients.append(a)
result = 0
for ai in coefficients:
    result = (result * X + ai) % MOD  

print(result)