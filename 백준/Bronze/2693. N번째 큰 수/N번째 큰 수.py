n = int(input())
for _ in range(n):
    arr = list(map(int, input().split()))
    arr.sort(reverse=True)
    print(arr[2])