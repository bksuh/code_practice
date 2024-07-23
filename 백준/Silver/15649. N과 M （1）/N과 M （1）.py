n, m = map(int, input().split())
arr = [i for i in range(1, n+1)]
import itertools

ans = list(itertools.permutations(arr, m))
for elem in ans:
    elem = list(elem)
    print(*elem, sep=' ')
