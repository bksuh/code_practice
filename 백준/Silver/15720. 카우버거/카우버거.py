b,c,d = map(int, input().split())
burger = list(map(int, input().split()))
side = list(map(int, input().split()))
soda = list(map(int, input().split()))
burger.sort()
side.sort()
soda.sort()
ans = 0
print(sum(burger) + sum(side) + sum(soda))

for i in range(min(b,c,d)):
    bur = burger.pop()
    so = side.pop()
    drin = soda.pop()
    ans += (bur+so+drin)*0.9

ans += sum(burger) + sum(side) + sum(soda)
print(int(ans))