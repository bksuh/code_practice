import sys
input = sys.stdin.readline
n = int(input())
d = {}
arr=list(map(int, input().split()))
for i in range(len(arr)):
    tmp = arr[i]
    d[tmp] = True

target = int(input())
cnt = 0

for i in range(len(arr)):
    try:
        if d[target - arr[i]] == True:
            cnt+=1
    except:
        continue
print(cnt//2)