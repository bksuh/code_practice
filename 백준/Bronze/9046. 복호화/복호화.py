t = int(input())

for _ in range(t):
    t = [c for c in input()]
    keys = set(t)
    counts = []
    for key in keys:
        if key == ' ':
            continue
        tmp = t.count(key)
        counts.append((key, tmp))
    counts.sort(key = lambda x:(-x[1]) )
    ans = counts[0][1]
    cnt = 0
    for i in range(1, len(counts)):
        if counts[i][1] == ans:
            cnt += 1
        else:
            break
    if cnt == 0:
        print(counts[0][0])
    else:
        print("?")
