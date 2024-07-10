n = int(input())
for _ in range(n):
    arr = list(input().split())
    if arr[0] == 'Simon' and arr[1] == 'says':
        print(' '+' '.join(arr[2:]))
