import sys
input = sys.stdin.readline
n = int(input())
arr = list(map(int, input().split()))
tmp=''
for i in range(len(arr)):
    tmp += str(arr[i])
ans = tmp.split('0')
result = 0
for i in range(len(ans)):
    n = len(ans[i])
    result += n*(n+1)//2

print(result)