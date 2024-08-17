tar = input()
t = len(tar)
pick = []
for i in range(1, t-1):
    for j in range(i+1, t):
        a = tar[:i]
        b = tar[i:j]
        c = tar[j:]
        a = a[::-1]
        b = b[::-1]
        c = c[::-1]
        ans = a+b+c
        pick.append(ans)
pick.sort()
print(pick[0])