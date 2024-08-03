n , m = map(int, input().split())

graph = []
for _ in range(n):
    tmp = list(map(int, input().split()))
    graph.append(tmp)

ans = []
for i in range(n-2):
    for j in range(m-2):
        tmp = []
        tmp.extend(graph[i][j:j+3])
        tmp.extend(graph[i+1][j:j+3])
        tmp.extend(graph[i+2][j:j+3])
        tmp.sort()
        ans.append(tmp[4])
cnt = 0
T = int(input())
for elem in ans:
    if elem >= T:
        cnt += 1

print(cnt)