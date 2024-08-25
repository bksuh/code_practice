import heapq
heap = []
tmp = list(map(int, input().split()))

n = tmp[0]
real = tmp[1::]
while len(real) != n:
        tmp = list(map(int, input().split()))
        real.extend(tmp)
for elem in real:
    rev = int(str(elem)[::-1])
    heapq.heappush(heap, rev)
while heap:
    print(heapq.heappop(heap))