import math


d, h, w = map(int, input().split())
k = math.sqrt(d**2 / (h**2 + w**2))
real_h = int(k * h)
real_w = int(k * w)
print(real_h, real_w)
