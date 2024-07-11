arr = [1, 0, 0]

move = input()
for c in move:
    if c == 'A':
        tmp = arr[0]
        arr[0] = arr[1]
        arr[1] = tmp
    elif c == 'B':
        tmp = arr[1]
        arr[1] = arr[2]
        arr[2] = tmp
    else:
        tmp = arr[0]
        arr[0] = arr[2]
        arr[2] = tmp
print(arr.index(1)+1)