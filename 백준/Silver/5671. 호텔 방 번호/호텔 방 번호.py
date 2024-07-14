while True:
    try:
        a, b = map(int, input().split())
        cnt = 0
        for i in range(a, b+1):
            tmp = [int(c) for c in str(i)]
            tmp.sort()
            tmp1 = list(set(tmp))
            tmp1.sort()
            if tmp == tmp1:
                cnt+=1
        print(cnt)
    except:
        break