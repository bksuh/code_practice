import sys
input = sys.stdin.readline

n = int(input())
arr=[]
ans = []
for _ in range(n):
    x = tuple(map(int, input().split()))
    arr.append(x)



for i in range(len(arr)):
    cnt = 0
    for j in range(len(arr)):
        if i==j:
            pass
        x1 , y1 = arr[i]
        x2, y2 = arr[j]
        if x1< x2 and y1 < y2:
            cnt +=1
    ans.append(cnt+1)

print(*ans)