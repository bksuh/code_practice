while True:
    a = int(input())
    if a == 0:
        break
    while True:
        if len(str(a)) == 1:
            break
        tmp = [int(c) for c in str(a)]
        a = sum(tmp)
    print(a)