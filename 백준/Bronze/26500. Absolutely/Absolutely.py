t = int(input())
for _ in range(t):
    a, b = map(float, input().split())
    ans = abs(b-a)
    ans = round(ans, 1)
    print(ans)