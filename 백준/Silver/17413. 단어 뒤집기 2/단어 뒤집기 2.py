tmp = input()
arr = []
flag = False
for c in tmp:
    if c == '<':
        print(*arr[::-1], sep='',end='')
        arr = []
        flag = True
    if c == '>':
        flag = False
        print(c, end='')
        continue
    if flag:
        print(c, end='')
        continue
    if c == ' ':
        print(*arr[::-1],sep='', end=' ')
        arr = []
        continue 
    arr.append(c)
print(*arr[::-1],sep='', end=' ')