import sys
input = sys.stdin.readline
n, m = map(int, input().split())
d1={}
d2={}
for i in range(1,n+1):
    name = input().rstrip()
    d1[i] = name
    d2[name] = i

for _ in range(m):
    tmp = input().rstrip()
    if tmp.isdigit():
        print(d1[int(tmp)])
    else:
        print(d2[tmp])