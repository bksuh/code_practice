import heapq, sys
input = sys.stdin.readline

n, t = map(int, input().split())
start = int(input())
graph = [[] for _ in range(n+1)]
INF = int(1e9)
heap = []
distance = [INF] *(n+1)

for _ in range(t):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))


def dijkstra(start):
    distance[start] = 0
    heapq.heappush(heap, (0, start))
    while heap:
        weight, now = heapq.heappop(heap)
        if distance[now] < weight:
            continue
        for next_node, w in graph[now]:
            next_weight = weight + w
            if next_weight < distance[next_node]:
                distance[next_node] = next_weight
                heapq.heappush(heap, (next_weight, next_node))

dijkstra(start)

for i in range(1, n+1):
    if distance[i] == INF:
        print("INF")
    else:
        print(distance[i])
