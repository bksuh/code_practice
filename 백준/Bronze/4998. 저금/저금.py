while True:
    try:
        n, b, m = map(float, input().split())
        cnt = 0
        while True:
            if n * pow(1 + b/100, cnt) > m:
                break
            cnt+=1
        print(cnt)
    except:
        break