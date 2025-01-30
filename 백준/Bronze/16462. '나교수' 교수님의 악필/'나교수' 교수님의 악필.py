import math

n = int(input())
ans = 0

for _ in range(n):
    t = input()
    while '0' in t or '6' in t:
        if '0' in t:
            t = t.replace('0', '9')
        else:
            t = t.replace('6', '9')
    tmp = int(t)
    if tmp >= 100:
        tmp = 100
    ans += tmp
ans = ans/n
print(round(ans + 0.0000001))