while True:
    a = input().lower()
    arr = [0 for _ in range(ord('z') - ord('a') + 1)]
    if a == '#':
        break
    for c in a:
        if c == ' ':
            continue
        elif c.isalpha():
            arr[ord(c)-ord('a')] = 1
    print(arr.count(1))
