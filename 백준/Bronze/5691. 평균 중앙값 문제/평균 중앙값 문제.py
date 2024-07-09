while True:
    a, b = map(int, input().split())
    arr = []
    if a==0 and b==0:
        break
    if 2*a-b == min(a, b, 2*a-b):
        print(2*a-b)
    elif a-2*b == max(a, b, a-2*b):
        print(a-2*b)
    else:
        print((a+b)//2)
