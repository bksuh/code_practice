import sys
import collections

input = sys.stdin.readline
n, k = map(int, input().split())
room = [[0]*2 for _ in range(6)]

for _ in range(n):
    s, g = map(int, input().split())
    room[g-1][s] +=1

ans = 0
for i in range(6):
    for j in range(2):
        if room[i][j] % k == 0 and room[i][j] != 0:
            ans+=(room[i][j]//k)
        elif room[i][j] % k != 0 and room[i][j] != 0:
            ans+=(room[i][j]//k +1)
print(ans)
