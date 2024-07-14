n = int(input())
names = [input() for _ in range(n)]
a = sorted(names)
b = sorted(names, reverse = True)

if names == a:
    print("INCREASING")
elif names == b:
    print("DECREASING")
else:print('NEITHER')