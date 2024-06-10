n = int(input())
arr = list(map(int, input().split()))
t, p = map(int, input().split())
ans1 = 0
for i in range(len(arr)):
    ans1 += arr[i]//t
    if arr[i]%t>0:
        ans1+=1
print(ans1)
print(n//p, n%p)