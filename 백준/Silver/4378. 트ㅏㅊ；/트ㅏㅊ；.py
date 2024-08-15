keys = list("`1234567890-=QWERTYUIOP[]\\ASDFGHJKL;'ZXCVBNM,./")

while True:
    try:
        ans = ''
        tar = input()

        for c in tar:
            if c == ' ':
                ans += ' '
            else:
                ans += keys[keys.index(c) - 1]
        print(ans)
    except:
        break