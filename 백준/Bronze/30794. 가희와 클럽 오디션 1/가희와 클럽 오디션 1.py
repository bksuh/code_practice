a, b = input().split()
a = int(a)

if b == 'miss':
    print(0)
elif b == 'bad':
    print(200*a)
elif b == 'cool':
    print(400*a)
elif b == 'great':
    print(600*a)
else:
    print(1000*a)