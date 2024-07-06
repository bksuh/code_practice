n = int(input())
for i in range(n):
    arr = list(map(int, input().split()))
    arr = arr[1:]
    print(f"Class {i+1}")
    arr.sort()
    tmp =[]
    for i in range(len(arr)-1):
        tmp.append(arr[i+1]- arr[i])
    print(f"Max {max(arr)}, Min {min(arr)}, Largest gap {max(tmp)}")