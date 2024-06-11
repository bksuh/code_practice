import sys

n = int(sys.stdin.readline())
arr=[0]*10001

for _ in range(n):
    tmp = int(sys.stdin.readline())
    arr[tmp]+=1
    
for i in range(len(arr)):
    if arr[i]==0:
        pass
    for _ in range(arr[i]):
        print(i)