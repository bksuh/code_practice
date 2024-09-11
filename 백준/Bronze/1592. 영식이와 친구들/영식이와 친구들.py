n, m, l = map(int, input().split())

import collections
student = collections.deque([0 for _ in range(n)])
student[0] = 1
cnt = 0
while True:
    if student[0] >= m:
        break
    if student[0] % 2 ==0:
        student.rotate(-l)
    else:
        student.rotate(l)
    cnt += 1
    student[0]+=1
print(cnt)
