import collections

n, m = map(int, input().split())
s = input()

if s.count('A') >= 2 and s.count('A')!= len(s):
    t = collections.deque(['A', 'A'])
    a_cnt = 2
    for c in s:
        if len(t) == m:
            break
        if c == 'A' and a_cnt != 0:
            a_cnt -= 1
            continue
        if c not in ['A', 'E', 'I', 'O', 'U'] and len(t) <= 3:
            t.append(c)
        else:
            t.appendleft(c)
            
            
    print("YES")
    t = list(t)
    print(''.join(t))
else:
    print("NO")