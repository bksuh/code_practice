import sys
input = sys.stdin.readline

t = int(input())
dfile = {}
for _ in range(t):
    name, ext = input().rstrip().split('.')
    if ext in dfile:
        dfile[ext] += 1
    else:
        dfile[ext] = 1
ans = [(k,v) for k, v in dfile.items()]
ans.sort(key=lambda x: x[0])
for k,v in ans:
    print(k, v)