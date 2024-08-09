while True:
    try:
        A,B,C = map(int, input().split())


        d = max(B - A, C - B)

        print(d - 1)
    except:
        exit()