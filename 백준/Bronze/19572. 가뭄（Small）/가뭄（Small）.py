x, y, z= map(int, input().split())

a = (x+y-z)/2
c = (-x + y+ z)/2
b = (x-y+z)/2

if a>0 and b>0 and c>0 :
    print(1)
    print(a, b, c)
else:
    print(-1)
