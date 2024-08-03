arr = ['-', '\\', '(', '@', '?', '>', '&', '%']
while True:
    tmp = input()
    if tmp == '#':
        break
    tmp = reversed(tmp)
    ans = 0
    for i, c in enumerate(tmp):
        if c in arr:
            ans += arr.index(c) * pow(8,i)
        else:
            ans += -pow(8, i)
    print(ans)