n, m = map(int, input().split())
arr = list(map(int, input().split()))
ans = 0
for i in range(1, n+1):
    for elem in arr:
        if i% elem == 0:
            ans += i
            break
print(ans)