while True:
    tar = input()
    if tar == '0':
        break
    cnt = 0
    while True:
        if len(tar) == 1:
            break
        tmp = list(int(c) for c in tar)
        tar = str(sum(tmp))
 
    print(int(tar))
