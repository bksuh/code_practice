n = int(input())
level = [int(input()) for _ in range(n)]
level.reverse()
ans = 0

for i in range(len(level)-1):
    if level[i]>level[i+1]:
        continue
    ans += level[i+1] - (level[i] -1)
    level[i+1] = level[i]-1
print(ans)