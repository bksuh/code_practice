import sys
import collections

input = sys.stdin.readline

while True:
    tmp = input().rstrip()
    if tmp =='.':
        break
    dq = collections.deque()
    for i in range(len(tmp)):
        if tmp[i] == '[' or tmp[i] =='(':
            dq.append(tmp[i])
        elif tmp[i] ==']' :
            if len(dq) !=0 and dq[-1] =='[':
                dq.pop()
            else:
                dq.append(tmp[i])
        elif tmp[i] ==")":
            if len(dq) !=0 and dq[-1] =='(':
                dq.pop()
            else:
                dq.append(tmp[i])
    if len(dq) == 0:
        print('yes')
    else:
        print('no')