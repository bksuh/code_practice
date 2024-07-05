n = int(input())
for i in range(n):
    x, y = 0, 0
    t = int(input())
    for _ in range(t):
        a, b = input().split()
        x+= int(a)
        y+= (float(b)*int(a))
    print(f"{x} {y/x:.1f}")