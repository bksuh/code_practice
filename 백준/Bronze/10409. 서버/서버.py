n , T = map(int, input().split())
arr = list(map(int, input().split()))
cnt = 0
tmp = 0
for i in range(len(arr)):
    if tmp + arr[i] <= T:
        cnt +=1
        tmp += arr[i]
    else:
        break
print(cnt)