import sys
input = sys.stdin.readline

n, m = map(int, input().split())
d={}
for _ in range(n):
    tmp = input().rstrip()
    if len(tmp) >= m:
        if tmp in d:
            d[tmp][0] +=1
        else:
            d[tmp] = [1, len(tmp)]
ans = list((v[0], v[1],k) for k,v in d.items())
ans.sort(key= lambda x : (-x[0], -x[1], x[2]))
for res in ans:
    print(res[2])