while True:
    tmp = list(map(int, input().split()))
    if tmp == [-1]:
        break
    tmp.sort()
    cnt = 0
    for i in range(1, len(tmp)):
        if 2*tmp[i] in tmp:
            cnt +=1
    print(cnt)