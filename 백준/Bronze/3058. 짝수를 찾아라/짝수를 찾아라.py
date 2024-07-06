n = int(input())
for _ in range(n):
    arr = list(map(int, input().split()))
    arr1 = []
    for i in range(len(arr)):
        if arr[i]%2==0:
            arr1.append(arr[i])
    print(sum(arr1),min(arr1))