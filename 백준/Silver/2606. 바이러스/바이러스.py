computer_num = int(input())
infos = [[] for _ in range(computer_num+1)]
n = int(input())
for _ in range(n):
    a,b = map(int, input().split())
    infos[a].append(b)
    infos[b].append(a)

visited = [False] * (computer_num+1)
area = 0
v= 1
def dfs(infos, visited, v):
    visited[v] = True
    for i in infos[v]:
        if not visited[i]:
            dfs(infos, visited, i)
dfs(infos, visited, v)

print(visited.count(True)-1)