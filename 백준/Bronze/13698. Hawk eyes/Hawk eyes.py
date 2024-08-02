arr = [1, 0, 0, -1]

what = input()
for c in what:
    if c =='A':
        tmp = arr[0]
        arr[0] = arr[1]
        arr[1] = tmp
    elif c =='B':
        tmp = arr[0]
        arr[0] = arr[2]
        arr[2] = tmp
    elif c =='C':
        tmp = arr[0]
        arr[0] = arr[3]
        arr[3] = tmp
    elif c =='D':
        tmp = arr[1]
        arr[1] = arr[2]
        arr[2] = tmp
    elif c =='E':
        tmp = arr[1]
        arr[1] = arr[3]
        arr[3] = tmp
    else:
        tmp = arr[2]
        arr[2] = arr[3]
        arr[3] = tmp
print(arr.index(1)+1)
print(arr.index(-1)+1)
