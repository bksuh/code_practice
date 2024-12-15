w, n, p = map(int, input().split())
arr = list(map(int, input().split()))

cnt = 0
for punch in arr:
    if w <= punch <= n:
        cnt += 1
print(cnt)