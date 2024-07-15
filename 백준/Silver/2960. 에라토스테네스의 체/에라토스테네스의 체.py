import collections
n, k = map(int, input().split())
ans = []
arr = collections.deque(i for i in range(2, n+1))

while len(arr) > 0:
    p = min(arr)
    for _ in range(len(arr)):
        if arr[0] % p == 0:
            ans.append(arr.popleft())
        else:
            arr.append(arr.popleft())
print(ans[k-1])