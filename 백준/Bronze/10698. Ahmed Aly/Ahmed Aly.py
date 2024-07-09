n = int(input())
for _ in range(n):
    a = input()
    x, y = a.split('=')
    if eval(x) == int(y):
        print(f"Case {_+1}: YES")
    else:
        print(f"Case {_+1}: NO")