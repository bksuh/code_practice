import math
n = int(input())
m = int(input())
arr=[]

a, b = pow(n, 1/2), pow(m, 1/2)
for i in range(int(a), int(b)+1):
    if n<=pow(i,2) and pow(i,2) <=m:
        arr.append(pow(i,2))

if arr:
    print(sum(arr))
    print(min(arr))
else:
    print(-1)