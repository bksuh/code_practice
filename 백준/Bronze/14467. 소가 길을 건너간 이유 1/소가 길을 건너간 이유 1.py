cows = {}
t = int(input())
cnt = 0

for _ in range(t):
    cow, loc = map(int, input().split())
    if cow not in cows.keys():
        cows[cow] = loc
    elif cows[cow] != loc:
        cows[cow] = loc
        cnt +=1
print(cnt)