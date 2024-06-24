import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
tmp =[]
for i in range(len(arr)):
    tmp.insert(arr[i], i+1)
tmp.reverse()
print(*tmp)