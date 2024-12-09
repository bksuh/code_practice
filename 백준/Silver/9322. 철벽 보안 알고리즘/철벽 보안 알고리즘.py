n = int(input())
for _ in range(n):
    t = int(input())
    ans = input().split()
    keys = input().split()
    message = input().split()

    picks = []
    for i in range(len(keys)):
        tmp = keys.index(ans[i])
        picks.append(tmp)

    for i in range(len(picks)):
        print(message[picks[i]], end = ' ')