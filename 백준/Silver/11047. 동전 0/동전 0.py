n, target = map(int, input().split())
got = list(int(input()) for _ in range(n))
got.reverse()
cnt = 0
for coin in got:
    cnt += (target//coin)
    target %=coin
    if target == 0:
        break
print(cnt)