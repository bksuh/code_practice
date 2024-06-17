n = int(input())
arr = list(int(input()) for _ in range(n))
arr.sort()
for i in range(len(arr)):
    print(arr[i])