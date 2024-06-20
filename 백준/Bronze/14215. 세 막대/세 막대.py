a = list(map(int, input().split()))
a = sorted(a)
x = a.pop(-1)
y,z = a
if y+z > x:
    print(x+y+z)
else:
    print(2*(y+z) -1)