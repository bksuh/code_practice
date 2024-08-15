n, x, y = map(int, input().split())
graph = []
for _ in range(n):
    tmp = list(map(int, input().split()))
    graph.append(tmp)
score = graph[x-1][y-1]
indi = True
for i in range(n):
    if i == x-1:
        for j in range(n):
            if j == y-1:
                continue
            else:
                if graph[x-1][j] > score:
                    indi = False
                    break
    else:
        if graph[i][y-1] > score:
            indi = False
            break
print('HAPPY' if indi else 'ANGRY')