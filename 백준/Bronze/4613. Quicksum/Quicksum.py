while True:
    target = input()
    if target == '#':
        break
    ans = 0
    for i in range(len(target)):
        if target[i] == ' ':
            continue
        ans += ((i+1)*(ord(target[i])-ord('A')+1))
    print(ans)