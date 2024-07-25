n, m = map(int, input().split())
ans = n
tmp = n
while True:
    if tmp // m == 0:
        break
    tmp = tmp // m
    ans+=tmp
print(ans)