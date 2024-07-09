n = int(input())
for i in range(n):
    arr = list(map(int, input().split()))
    arr.sort()
    a, b, c = arr
    print(f"Case #{i+1}: ", end="")
    if a+b <= c:
        print("invalid!")
    elif a==b and b==c and c==a:
        print("equilateral")
    elif a!=b and b!=c and c!=a:
        print("scalene")
    else:
        print("isosceles")