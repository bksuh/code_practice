a ,b= 0,0
a1 = [int(input()) for _ in range(3)]
b1 = [int(input()) for _ in range(3)]

for i,v in enumerate(a1):
    a += (3-i) * v
for i,v in enumerate(b1):
    b += (3-i) * v

if a > b:
    print("A")
elif a == b:
    print("T")
else:
    print('B')