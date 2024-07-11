arr = list(map(int, input().split()))
tmp = sorted(arr)
while True:
    for i in range(len(arr)-1):
        if arr[i] > arr[i+1]:
            a = arr[i+1]
            arr[i+1] = arr[i]
            arr[i] = a
            print(*arr)


    if arr == tmp:
        break