n = int(input())
arr = [(0,0), (0,1)]

for i in range(n-1):
    arr.append((arr[-1][1],arr[-1][0]+arr[-1][1]))

x, y = arr[-1]
print(x, y)