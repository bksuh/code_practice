while True:
    target = input()
    if target == '0':
        break
    print(target, end=' ')
    while True:
        if len(target) == 1:
            break
        arr = [int(c) for c in target]
        mult = 1
        for element in arr:
            mult *=element
        target = str(mult)
        print(mult, end =' ')
    print()