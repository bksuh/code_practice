n = int(input())
for _ in range(n):
    d = {}
    t = int(input())
    for _ in range(t):
        a, b = input().split()
        b = int(b)
        if a not in d.keys():
            d[a] = b
        else:
            d[a] += b
    arr = [(k, v) for k, v in d.items()]
    sorted_arr = sorted(arr, key=lambda x: -x[1])
    print(sorted_arr[0][0])


