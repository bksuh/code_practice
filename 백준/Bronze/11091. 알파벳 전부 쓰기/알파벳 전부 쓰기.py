n = int(input())
for _ in range(n):
    arr = [1 for _ in range(ord('z')- ord('a')+1)]
    a = input().lower()
    for c in a:
        if c.isalpha():
            arr[ord(c)-ord('a')] = 0
    if max(arr) == 0:
        print('pangram')
    else:
        print('missing ', end='')
        for i in range(len(arr)):
            if arr[i] == 1:
                print(chr(ord('a')+i), end = '')
        print()
