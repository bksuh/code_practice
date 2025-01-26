while True:
    try:
        a, b = map(int, input().split())
        ans = b//(a+1)
        print(ans)
    except:
        break