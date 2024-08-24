n, total = map(int, input().split())
picks = []
for _ in range(n):
    p, l = map(int, input().split())
    points = list(map(int, input().split()))
    if p < l:
        picks.append(1)
    elif p == l:
        picks.append(min(points))
    else:
        points.sort(reverse=True)
        picks.append(points[l-1])

picks.sort()
cnt = 0
for score in picks:
    total -= score
    if total < 0:
        break
    cnt+=1
print(cnt)
