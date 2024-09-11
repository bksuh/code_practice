from collections import deque
a, b = map(int, input().split())
current = input()
passing = [' ', '.', ',']
up = deque([chr(a) for a in range(ord('A'), ord('Z')+1)])
low = deque([chr(a) for a in range(ord('a'), ord('z')+1)])

up.rotate(-a)
low.rotate(-a)
ans =''
for c in current:
    if c in passing:
        ans+=c
        continue
    if c.isupper():
        tmp = ord(c)-ord('A')
        ans += up[tmp]
    else:
        tmp = ord(c)-ord('a')
        ans += low[tmp]
print(ans)