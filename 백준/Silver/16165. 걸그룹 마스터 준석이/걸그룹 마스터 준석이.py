import sys
input = sys.stdin.readline

n, m = map(int, input().split())
data = {}
for _ in range(n):
    team_name = input().rstrip()
    group = [input().rstrip() for _ in range(int(input()))]
    data[team_name] = group

for _ in range(m):
    x = input().rstrip()
    y = int(input())
    if y == 0:
        tmp = data[x]
        tmp.sort()
        print(*tmp, sep='\n')

    else:
        for k,v in data.items():
            if x in data[k]:
                print(k)
                break