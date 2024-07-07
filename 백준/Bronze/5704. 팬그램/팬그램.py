while True:
    arr = [1 for _ in range(ord('z')- ord('a')+1)]
    a = input()
    if a == '*':
        break
    for c in a:
        if c == ' ':
            continue
        arr[ord(c)-ord('a')] = 0
    print('N' if max(arr) == 1 else'Y' )
    
