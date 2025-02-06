n = int(input())
arr = list(map(int, input().split()))

ans = 0
sum_len = 0
for i in range(len(arr)-1, 0, -1):
    sum_len += arr[i]
    ans += (sum_len*arr[i-1])
print(ans)