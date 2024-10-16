a, b, c = map(int, input().split())
t = int(input())

ans = -1
for _ in range(t):
    tmp = 0
    for _ in range (3):
        x, y , z = map(int, input().split())
        tmp += (a*x + b*y + c*z)
    ans = max(ans, tmp)
print(ans)