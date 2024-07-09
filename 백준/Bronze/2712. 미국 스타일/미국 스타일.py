n = int(input())
for _ in range(n):
    a, b = input().split()
    a = float(a)
    if b == 'kg':
        print(f"{a*2.2046:.4f} lb")
    elif b =='lb':
        print(f"{a*0.4536:.4f} kg")
    elif b =='l':
        print(f"{a*0.2642:.4f} g")
    else:
        print(f"{a*3.7854:.4f} l")