d, p = 0, 0
t = int(input())

for _ in range(t):
    score = input()
    if abs(d-p) >= 2:
        continue
    elif score == 'D':
        d += 1
    else:
        p += 1

print(f"{d}:{p}")