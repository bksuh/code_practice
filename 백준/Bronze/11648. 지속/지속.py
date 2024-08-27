tmp = [int(c) for c in input()]
cnt = 0
while True:
    if len(tmp) == 1:
        print(cnt)
        break
    ans = 1
    for num in tmp:
        ans *= num
    tmp = [int(c) for c in str(ans)]
    cnt += 1