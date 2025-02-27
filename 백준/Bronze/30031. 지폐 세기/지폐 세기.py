n = int(input())
total = 0

for _ in range(n):
    a, b = map(int, input().split())
    if b == 68:
        if a == 136:
            total += 1000
        elif a == 142:
            total += 5000
        elif a == 148:
            total += 10000
        elif a == 154:
            total += 50000

print(total)