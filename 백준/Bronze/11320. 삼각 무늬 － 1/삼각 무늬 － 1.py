n = int(input())
for _ in range(n):
    a, b = map(int, input().split())
    ans = a//b
    print(pow(ans, 2))