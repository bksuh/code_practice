n = int(input())
arr =[]
for _ in range(n):
    a = tuple(map(int, input().split()))
    arr.append(a)
arr = sorted(sorted(arr, reverse=True))
for element in arr:
    print(element[0], element[1])
