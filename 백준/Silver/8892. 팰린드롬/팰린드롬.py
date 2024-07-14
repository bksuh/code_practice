n = int(input())

for _ in range(n):
    t = int(input())
    arr = list(input() for _ in range(t))
    indi = False
    for i in range(len(arr)):
        for j in range(len(arr)):
            if i==j:
                continue
            tmp = arr[i]+arr[j]

            if tmp == tmp[::-1]:
                indi = True
                print(tmp)
                break
        if indi:
            break
    if not indi:
        print(0)