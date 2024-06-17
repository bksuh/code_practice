import sys
input = sys.stdin.readline
n , m = map(int, input().split())
arr = list(i for i in range(1, n+1))
for _ in range(m):
    a , b = map(int, input().split())
    tmp = arr[a-1]
    arr[a-1] = arr[b-1]
    arr[b-1] = tmp
print(*arr)