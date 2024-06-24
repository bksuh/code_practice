import sys
input = sys.stdin.readline

n = int(input())
arr1 = list(map(int, input().split()))
m = int(input())
tmp = list(map(int,input().split()))
d={}
for i in range(len(tmp)):
    d[tmp[i]] = 0

for i in range(len(arr1)):
    if arr1[i] in d.keys():
        d[arr1[i]] = 1

ans = list(d.values())

print(*ans)