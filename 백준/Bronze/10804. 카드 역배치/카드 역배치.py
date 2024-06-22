arr = list(i for i in range(1,21))

for _ in range(10):
    a, b = map(int, input().split())
    tmp = arr[a-1:b]
    tmp.reverse()
    arr[a-1:b] = tmp

print(*arr)