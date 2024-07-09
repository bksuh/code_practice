a, b = map(int, input().split())
ax = a//4
ay = a%4
if ay == 0:
    ay = 3
    ax-=1
else: ay -=1

bx = b//4
by = b%4
if by == 0:
    by = 3
    bx -=1
else: by -=1

ans = abs(bx-ax) + abs(by-ay)
print(ans)