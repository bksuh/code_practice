n = int(input())
s = input()

cnt1, cnt2 = 0, 0

for i in range(len(s)):
    if int(s[i]) %  2 == 0:
        cnt1 += 1
    else:
        cnt2 += 1

if cnt1 - cnt2 > 0:
    print(0)
elif cnt1 - cnt2 < 0:
    print(1)
else:
    print(-1)