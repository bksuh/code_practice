import heapq
INF = int(1e9)
n = int(input())
t = int(input())
distance = [INF]*(n+1)
heap = []
graph = [[] for _ in range(n+1)]
for _ in range(t):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

def djikstra(start):
    distance[start] = 0
    heapq.heappush(heap, (0, start))
    while heap:
        weight, now = heapq.heappop(heap)
        if distance[now] < weight:
            continue
        for next_node in graph[now]:
            next_weight = weight + 1
            if next_weight < distance[next_node]:
                distance[next_node] = next_weight
                heapq.heappush(heap,(next_weight, next_node))
djikstra(1)
ans = 0
for i in range(2, len(distance)):
    if distance[i] <= 2:
        ans+=1
print(ans)