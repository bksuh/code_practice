import math
import sys
input = sys.stdin.readline
def round_cos (x):
    if x - math.floor(x) >= 0.5:
        return math.ceil(x)
    else:
        return math.floor(x)

n = int(input())
if n == 0:
    print(0)
else:
    picks = list(int(input()) for _ in range(n))
    picks.sort()
    many = round_cos(n*.15)
    tmp = picks[many: n-many]
    print(round_cos(sum(tmp)/len(tmp)))
