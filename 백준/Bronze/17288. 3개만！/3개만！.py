a = input()
ans = 0

start = int(a[0]) + 1
cnt = 1
for i in range(1, len(a)):
    if int(a[i]) == start:
        start +=1
        cnt += 1
    elif cnt == 3:
        ans += 1
        cnt = 1
        start = int(a[i]) + 1
    else:
        start = int(a[i]) + 1
        cnt = 1
if cnt == 3 and start-1 == int(a[-1]):
    ans += 1
print(ans)