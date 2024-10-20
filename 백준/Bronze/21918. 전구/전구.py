a, b = map(int, input().split())
lightbulb = list(map(int, input().split()))
for _ in range(b):
    x, y, z = map(int, input().split())
    if x == 1:
        lightbulb[y-1] = z
    elif x ==2:
        for k in range(y-1, z):
            if lightbulb[k] == 1:
                lightbulb[k] = 0
            else:
                lightbulb[k] = 1
    elif x == 3:
        for k in range(y-1, z):
            lightbulb[k] = 0
    
    else:
        for k in range(y-1, z):
            lightbulb[k] = 1

print(*lightbulb)