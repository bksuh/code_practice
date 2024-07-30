n = int(input())
arr =[0]
tmp = list(map(int, input().split()))
arr.extend(tmp)
t = int(input())

for _ in range(t):
    a = tuple(map(int, input().split()))
    if a[0] == 1:
        l, r, k = a[1], a[2], a[3]
        tmp = arr[l: r+1]
        print(tmp.count(k))
    else:
        l, r = a[1], a[2]
        for k in range(l, r+1):
            arr[k] = 0