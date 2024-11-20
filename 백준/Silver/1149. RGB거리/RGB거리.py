t = int(input())
colors = []
for _ in range(t):
    tmp = list(map(int, input().split()))
    colors.append(tmp)

for i in range(1, t):
    colors[i][0] += min(colors[i-1][1], colors[i-1][2])
    colors[i][1] += min(colors[i-1][0], colors[i-1][2])
    colors[i][2] += min(colors[i-1][0], colors[i-1][1])

print(min(colors[t-1]))