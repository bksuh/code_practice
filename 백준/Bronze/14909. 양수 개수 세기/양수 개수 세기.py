arr = list(map(int, input().split()))
cnt = 0
for i in range(len(arr)):
    if arr[i] > 0:
        cnt += 1
print(cnt)