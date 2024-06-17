n = int(input())
grid = list(tuple(map(int, input().split())) for _ in range(n))
gridx = sorted(grid, key = lambda x : x[0])
gridy = sorted(grid, key= lambda x : x[1])
w = gridx[n-1][0] - gridx[0][0]
h = gridy[n-1][1] - gridy[0][1]
print(w*h)