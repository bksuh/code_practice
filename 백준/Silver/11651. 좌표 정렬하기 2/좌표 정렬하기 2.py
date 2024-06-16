import sys
input = sys.stdin.readline

n = int(input())
points = []
for _ in range(n):
    x, y = map(int, input().split())
    points.append((x, y))

tmp = sorted(points, key = lambda x : (x[1], x[0]))
for i in range(len(tmp)):
    x, y = tmp[i][0], tmp[i][1]
    print(x, y)