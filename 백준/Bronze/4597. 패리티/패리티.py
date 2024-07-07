while True:
    a = input()
    if a == '#':
        break
    tar = a[:len(a)-1]
    if a[-1] == 'e':
        if tar.count('1') %2 == 0:
            print(tar+'0')
        else:
            print(tar+'1')
    elif a[-1] == 'o':
        if tar.count('1') %2 == 1:
            print(tar+'0')
        else:
            print(tar+'1')