n = int(input())

for _ in range(n):
    a, b, x = map(int, input().split())
    ans = a*(x-1) + b
    print(ans)