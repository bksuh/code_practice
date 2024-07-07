n = int(input())

for _ in range(n):
    a = input()
    b = a[::-1]
    tmp1 = int(a) + int(b)
    if str(tmp1) == str(tmp1)[::-1]:
        print("YES")
    else:
        print("NO")