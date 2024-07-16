while True:
    try:
        s, t = input().split()
        cnt = 0
        max_cnt = len(s)
        ans = ''
        for i in range(len(t)):
            if t[i] == s[cnt]:
                ans+=t[i]
                cnt+=1
            if cnt == max_cnt:
                break
            else:
                continue
        if ans == s:
            print('Yes')
        else:
            print('No')
    except:
        break