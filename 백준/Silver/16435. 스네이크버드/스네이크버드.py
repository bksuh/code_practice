n, start = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()

for i in range(len(arr)):
    if arr[i] <= start:
        start +=1

print(start)