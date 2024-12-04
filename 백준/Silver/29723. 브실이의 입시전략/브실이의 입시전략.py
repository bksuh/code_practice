n, m , k = map(int, input().split())
sugang = {}
for _ in range(n):
    subject, score = input().split()
    sugang[subject] = int(score)

ans = 0
for _ in range(k):
    open_sub = input()
    a = sugang.pop(open_sub)
    ans += a

lookup = [(k, v) for k, v in sugang.items()]
lookup.sort(key=lambda x: -x[1])

ans1, ans2 = ans, ans

for i in range(m-k):
    ans1 += lookup[i][1]

lookup1 = lookup[::-1]
for j in range(m-k):
    ans2 += lookup1[j][1]

print(ans2, ans1)