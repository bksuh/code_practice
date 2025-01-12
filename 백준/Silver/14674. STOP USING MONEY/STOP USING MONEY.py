import sys
from functools import cmp_to_key
input = sys.stdin.readline


def compare(x, y):
    v1 = x[2] * y[1]
    v2 = x[1] * y[2]
    if v1 > v2:
        return -1
    elif v1 < v2:
        return 1
    else:
        if x[1] < y[1]:
            return -1
        elif x[1] > y[1]:
            return 1
        else:
            if x[0] < y[0]:
                return -1
            else:
                return 1


N, K = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
arr.sort(key=cmp_to_key(compare))
for i in range(K):
    print(arr[i][0])