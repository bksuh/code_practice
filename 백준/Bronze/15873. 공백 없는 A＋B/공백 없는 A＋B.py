a = input()
ans = 0
if len(a) == 2:
    tmp = int(a) // 10
    tmp1 = int(a) % 10
    ans = tmp + tmp1
elif len(a) == 3 and a[0] == '1' and a[1] == '0':
    ans = 10 + int(a[-1])
else:
    tmp = int(a) // 100
    ans = 10 + tmp

print(ans)