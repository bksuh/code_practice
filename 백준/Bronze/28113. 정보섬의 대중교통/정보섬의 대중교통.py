n, a, b = map(int, input().split())

a -= n
b -= n

if a == b:
    print("Anything")
elif a < b:
    print("Bus")
else:
    print("Subway")