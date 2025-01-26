arr = list(map(int, input().split()))
ans = 100000
for i in range(len(arr)-1):
    for j in range(i+1, len(arr)):
        tmp = sum(arr) - 2*(arr[i] + arr[j])
        if tmp >= 0:
            ans = min(ans, tmp)
print(ans)