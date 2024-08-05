n = int(input())
ans = 0
for a in range(1, n+1):
    tmp = str(a)
    ans += (tmp.count('3') + tmp.count("6") + tmp.count('9'))
print(ans)
