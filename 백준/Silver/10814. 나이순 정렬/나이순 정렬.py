n = int(input())
arr = []
for i in range(n):
    a, b = input().split()
    arr.append((int(a), b, i))
arr = sorted(arr, key = lambda x : (x[0], x[2]))
for i in range(len(arr)):
    print(arr[i][0], arr[i][1])