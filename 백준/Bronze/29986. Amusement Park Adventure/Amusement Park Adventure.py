ans = 0

n, t = map(int, input().split())
tmp = list(map(int, input().split()))

for h in tmp:
    if t >= h:
        ans += 1
        
print(ans)