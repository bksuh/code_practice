arr = list(map(int, input().split()))
ans = min(arr)
cnt = 0
while True:
    cnt = 0
    for elem in arr:
        if ans % elem == 0:
            cnt+=1
    if cnt >= 3:
        print(ans)
        break
    ans+=1
