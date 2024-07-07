a = input()

for c in a:
    if c=='A':
        print('X', end ='')
    elif c == 'B':
        print('Y', end ='')
    elif c == 'C':
        print('Z', end ='')
    else:
        tmp = ord(c)-3
        print(chr(tmp), end='')
