import sys
input = sys.stdin.readline

n, t = map(int, input().split())
arr = list(map(int, input().split()))
for i in range(1, len(arr)):
    arr[i] = arr[i] + arr[i-1]

for _ in range(t):
    a, b = map(int, input().split())
    if a==1:
        print(arr[b-1])
    else:
        print(arr[b-1] - arr[a-2])