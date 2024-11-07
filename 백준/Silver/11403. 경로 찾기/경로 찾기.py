t = int(input())
grid = []
for _ in range(t):
    tmp = list(map(int, input().split()))
    grid.append(tmp)


def floyd(graph):
    n = len(graph)
    reach = [[graph[i][j] for j in range(n)] for i in range(n)]
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if reach[i][k] and reach[k][j]:
                    reach[i][j] = 1
    return reach

ans = floyd(grid)
for elem in ans:
    print(*elem)
