target = list(input())
for i in range(len(target)):
    if target[i] == ' ':
        continue
    elif target[i].isupper():
        tmp = ord(target[i])+13
        if tmp > ord('Z'):
            tmp += (ord("A")-ord('Z')-1)
        target[i] = chr(tmp)
    elif target[i].islower():
        tmp = ord(target[i])+13
        if tmp > ord('z'):
            tmp += (ord('a')-ord('z')-1)
        target[i] = chr(tmp)
for elem in target:
    print(elem, end ='')