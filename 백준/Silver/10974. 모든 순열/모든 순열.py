import itertools

t = int(input())
tmp = [i for i in range(1,t+1)]
ans = list(itertools.permutations(tmp, t))
ans.sort()
for elem in ans:
    print(*elem)