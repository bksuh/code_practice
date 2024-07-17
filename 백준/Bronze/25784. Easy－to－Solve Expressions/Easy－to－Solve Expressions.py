a, b, c = map(int, input().split())
if a+b == c or a==b+c or b == a+c:
    print(1)
elif a*b == c or a == b*c or b == a*c:
    print(2)
else:
    print(3)