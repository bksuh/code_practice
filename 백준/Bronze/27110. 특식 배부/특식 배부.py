t = int(input())
arr = list(map(int, input().split()))
ans = 0
for elem in arr:
    if t >= elem:
        ans+= elem
    else:
        ans+= t
print(ans)