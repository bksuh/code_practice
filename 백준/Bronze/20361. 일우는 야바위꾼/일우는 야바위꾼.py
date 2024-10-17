n, a, t = map(int, input().split())
arr = [0]*(n+1)
arr[a] = 1
for _ in range(t):
    x, y = map(int, input().split())
    arr[x], arr[y] = arr[y], arr[x]
print(arr.index(1))