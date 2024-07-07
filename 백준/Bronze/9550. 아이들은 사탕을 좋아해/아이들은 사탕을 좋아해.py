n = int(input())
for _ in range(n):
    a, b = map(int, input().split())
    arr = list(map(int, input().split()))
    total = 0
    for elem in arr:
        total += (elem//b)
    print(total)