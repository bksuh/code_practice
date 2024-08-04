n, k = map(int, input().split())
arr = list(map(int, input().split()))
tmp = [0]*n
window = sum(arr[0:k])
ans = window
cnt = 1
if tmp == arr:
    print("SAD")
else:
    for i in range(n-k):
        window += arr[i+k] - arr[i]
        if window == ans:
            cnt += 1
        elif window > ans:
            cnt = 1
            ans = max(ans, window)
    print(ans)
    print(cnt)