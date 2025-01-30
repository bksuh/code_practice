n = int(input())
cnt1, cnt2 = 0, 0
x, y, r = map(int, input().split())

for _ in range(n):
    t = int(input())
    
    if t == x -r or t == x+r:
        cnt1 += 1
    elif x - r < t and t < x + r:
        cnt2 += 1

print(cnt2, cnt1)