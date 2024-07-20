import sys
input = sys.stdin.readline

n , t = map(int, input().split())
arr = {}
for _ in range(n):
    tmp = input()
    arr[tmp] = 0

for _ in range(t):
    tmp = input()
    if tmp in arr.keys():
        arr[tmp] +=1
ans = list(arr.values())
print(sum(ans))