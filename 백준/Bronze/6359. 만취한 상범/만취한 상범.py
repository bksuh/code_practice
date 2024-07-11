T = int(input())

for _ in range(T):
    tmp = int(input())
    arr = [0 for _ in range(tmp+1)]
    for i in range(1, tmp + 1):
        for j in range(1, tmp+ 1):
            if j%i == 0:
                if arr[j] == 0:
                    arr[j] = 1
                elif arr[j] == 1:
                    arr[j] = 0
    print(arr.count(1))