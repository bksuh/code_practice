import sys
input = sys.stdin.readline

n = int(input().rstrip())
ans = 0
picks = {}
for _ in range(n):
    com = input().rstrip()
    if com == 'ENTER':
        ans += len(picks.keys())
        picks = {}
    elif com not in picks.keys():
        picks[com] = 1
ans += len(picks.keys())
print(ans)