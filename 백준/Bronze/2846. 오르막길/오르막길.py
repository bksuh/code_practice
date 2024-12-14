t = int(input())
arr = list(map(int, input().split()))
diff = []
for i in range(1, len(arr)):
    tmp = arr[i] - arr[i-1]
    diff.append(tmp)

current = diff[0]
ans = []
for i in range(1, len(diff)):
    if diff[i] <= 0:
        ans.append(current)
        current = 0
    else:
        current += diff[i]
ans.append(current)
print(max(ans))