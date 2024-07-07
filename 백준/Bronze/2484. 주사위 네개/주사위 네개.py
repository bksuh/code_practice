n = int(input())
tmp = []

for _ in range(n):
    arr = list(map(int, input().split()))
    keys = set(arr)
    if len(keys) == 4:
        tmp.append(max(arr)*100)
    elif len(keys) == 1:
        tmp.append(50000 + 5000*list(keys)[0])
    elif len(keys) == 3:
        for key in keys:
            if arr.count(key) == 2:
                tmp.append(1000+100*key)
                break
    elif len(keys) == 2:
        indi = True
        for key in keys:
            if arr.count(key) == 3:
                tmp.append(10000 + 1000*key)
                indi = False
                break
        if indi:
            tmp.append(2000+500*(list(keys)[0]+list(keys)[1]))

print(max(tmp))