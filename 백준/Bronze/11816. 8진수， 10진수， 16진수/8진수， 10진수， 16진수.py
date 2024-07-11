n = input()
if len(n) == 1 or n[0] != '0':
    print(int(n))
else:
    if n[0:2] == '0x':
        print(int(n[2:], 16))
    else:
        print(int(n[1:], 8))