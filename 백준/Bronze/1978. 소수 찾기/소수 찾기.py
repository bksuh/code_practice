n = int(input())
arr = list(map(int,input().split()))
ans = 0

for i in range(len(arr)):
    cnt =0
    for j in range(1, arr[i]+1):
        if arr[i]%j ==0:
            cnt+=1
    if cnt == 2:
        ans+=1

print(ans)