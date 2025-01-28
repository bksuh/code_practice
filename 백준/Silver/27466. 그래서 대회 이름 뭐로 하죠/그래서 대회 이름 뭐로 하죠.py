from collections import deque

n, m = map(int, input().split())
s = deque(input()[::-1])
ans = deque([])
indi_x, indi_a = True, True
a = list('AEIOU')

for _ in range(len(s)):
    c = s.popleft()
    if indi_x and (c not in a) and len(ans) == 0:
        ans.appendleft(c)
        indi_x = False
    elif indi_a and c == 'A' and len(ans) <= 3:
        ans.appendleft(c)
        if len(ans) == 3:
            indi_a = False
    elif not indi_x and not indi_a:
        ans.appendleft(c)
        if len(ans) == m:
            break

if len(ans) == m:
    print('YES')
    print(''.join(ans))
else:
    print('NO')