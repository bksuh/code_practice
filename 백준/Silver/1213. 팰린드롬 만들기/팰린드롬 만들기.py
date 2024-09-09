import collections
alpha = list(input())
alpha.sort()
tmp = collections.Counter(alpha)

odd = 0
odd_alpha = ''
ans = ''
for i in tmp:
    if tmp[i] % 2 != 0:
        odd += 1
        odd_alpha += i
    for _ in range(tmp[i]//2):
        ans += i

if odd > 1:
    print("I'm Sorry Hansoo")
elif odd == 0:
    print(ans + ans[::-1])
else:
    print(ans + odd_alpha + ans[::-1])