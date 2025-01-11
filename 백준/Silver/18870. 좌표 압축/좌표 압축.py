n = int(input())
num = list(map(int, input().split()))
arr = sorted(set(num))

d = {arr[i]: i for i in range(len(arr))}

for elem in num:
    print(d[elem], end=' ')