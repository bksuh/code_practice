import math

a, b, c = map(int, input().split())

ans = math.floor(((a+1)*(b+1)/(c+1))-1)
print(ans)