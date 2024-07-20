import collections
tar = input()
tmp = collections.deque()
ans = 0
for i in range(len(tar)-1):
    if tar[i] =='(' and tar[i+1] =='(':
        tmp.append(tar[i])
    elif tar[i] ==')' and tar[i+1] == ')':
        tmp.pop()
        ans+=1
    elif tar[i] == '(' and tar[i+1] == ')':
        ans+=len(tmp)

print(ans)