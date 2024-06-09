while True:
    arr = list(map(int, input().split()))
    if  arr ==[0, 0, 0]:
        break
    c = max(arr)
    arr.remove(c)
    a, b= arr[0], arr[1]
    if c**2 == a**2 + b**2:
        print('right')
    else:
        print('wrong')
