import sys
input = sys.stdin.readline
n = int(input())
arr = []
for _ in range(n):
    tmp = input().rstrip()
    arr.append(tmp)

for i in range(len(arr)):
    if arr[i][::-1] in arr:
        print(len(arr[i]), arr[i][len(arr[i])//2])
        break