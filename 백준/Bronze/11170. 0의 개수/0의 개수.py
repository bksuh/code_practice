n = int(input())
for _ in range(n):
    a , b = map(int, input().split())
    cnt = 0
    for i in range(a, b+1):
        i = str(i)
        tmp = list(i)
        if '0' in tmp:
            cnt+=tmp.count('0')
        else:
            continue
    print(cnt)