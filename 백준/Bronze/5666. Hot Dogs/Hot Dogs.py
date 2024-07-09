while True:
    try:
        a, b = map(int, input().split())
        print(f"{a/b:.2f}")
    except:
        break