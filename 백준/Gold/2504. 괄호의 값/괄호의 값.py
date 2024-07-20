import collections
tar = input()
tmp = collections.deque()
ans = 1
if tar[0] == ']' or tar[0] == ')':
    ans = 0
else:
    for c in tar:
        if c == '(' or c == '[':
            tmp.append(c)
        elif c == ')' and tmp[-1] == '(':
            tmp.pop()
            tmp.append(2)
        elif c == ']' and tmp[-1] == '[':
            tmp.pop()
            tmp.append(3)
        elif c == ')' and len(tmp)>=2 and isinstance(tmp[-1], int) and tmp[-2] == '(':
            t = tmp.pop()
            tmp.pop()
            tmp.append(2*t)
        elif c == ']' and len(tmp)>=2 and isinstance(tmp[-1], int) and tmp[-2] == '[':
            t = tmp.pop()
            tmp.pop()
            tmp.append(3*t)
        else:
            tmp.append(c)
        
        if len(tmp) >=2 and isinstance(tmp[-1], int) and isinstance(tmp[-2], int):
            t1 = tmp.pop()
            t2 = tmp.pop()
            tmp.append(t1+t2)

if ans == 1 and len(tmp) == 1 and isinstance(tmp[0], int):
    print(tmp[0])
else:
    print(0)
        

