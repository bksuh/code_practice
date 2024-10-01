import math
x, y, r = map(int, input().split())
a, b, c = map(int, input().split())

d = (pow(x-a,2)+pow(y-b,2))
if pow(r+c,2) >d:
    print('YES')
else:
    print('NO')