n,m = tuple(map(int, input().split()))
arr = list(map(int, input().split()))
ans = 0
for i in range(len(arr)):
    for j in range(i, len(arr)):
        for k in range(j, len(arr)):
            if i==j or j==k or i==k:
                continue
            if arr[i]+arr[j]+arr[k]<=m:
                tmp = arr[i]+arr[j]+arr[k]
                ans = max(ans, tmp)
print(ans)