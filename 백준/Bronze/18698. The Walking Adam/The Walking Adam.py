t = int(input())

for _ in range(t):
    s = input()
    cnt = 0
    for c in s:
        if c =='U':
            cnt += 1
        else:
            break
    print(cnt)