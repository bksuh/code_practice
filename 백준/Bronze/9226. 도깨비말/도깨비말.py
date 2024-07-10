di = ['a', 'e', 'i','o','u']
while True:
    a = input()
    if a == '#':
        break
    tmp = 0
    for c in a:
        if c in di:
            tmp = a.index(c)
            break
    print(a[tmp:] + a[0:tmp]+'ay')