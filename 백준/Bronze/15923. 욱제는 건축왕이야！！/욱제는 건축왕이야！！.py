n = int(input())
points = []

for _ in range(n):
    point = tuple(map(int, input().split()))
    points.append(point)

ans = 0
sx, sy = points[0]

for x, y in points[1::]:
    distance = int(pow((sx-x)**2 + (sy-y)**2, 1/2))
    ans += distance
    sx, sy = x, y
last= int(pow((points[0][0]-x)**2 + (points[0][1]-y)**2, 1/2))

print(ans + last)