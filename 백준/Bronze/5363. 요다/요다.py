n = int(input())

for _ in range(n):
    arr = list(input().split())
    print(*(arr[2:]+arr[:2]))