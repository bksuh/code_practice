while True:
    t = int(input())
    if t == 0:
        break
    checks = [1 for _ in range(49)]
    for _ in range(t):
        arr = list(map(int, input().split()))
        for c in arr:
            checks[c-1] = 0
    if 1 in checks:
        print("No")
    else:
        print("Yes")
