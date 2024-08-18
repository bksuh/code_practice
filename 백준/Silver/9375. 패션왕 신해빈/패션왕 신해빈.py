n = int(input())
for _ in range(n):
    t = int(input())
    clothes = {}
    for _ in range(t):
        name, cloth = input().split()
        if cloth in clothes:
            clothes[cloth] += 1
        else:
            clothes[cloth] = 2
    ans = 1
    for k in clothes.values():
        ans *= k
    print(ans-1)