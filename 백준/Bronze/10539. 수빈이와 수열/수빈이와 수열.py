t = int(input())
arr = list(map(int, input().split()))
ans = [0 for _ in range(len(arr))]
for i in range(1, len(arr)+1):
    ans[i-1] = i*arr[i-1] - sum(ans[:i-1])
print(*ans)
