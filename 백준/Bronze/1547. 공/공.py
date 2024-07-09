arr = [1, 0, 0]
n = int(input())

for _ in range(n):
    a, b = map(int, input().split())
    a, b = a-1, b-1
    tmp = arr[a]
    arr[a] = arr[b]
    arr[b] = tmp

print(arr.index(1)+1)