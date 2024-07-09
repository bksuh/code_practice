n = int(input())
for _ in range(n):
    total = int(input())
    for t in range(int(pow(total, 1/2))+1):
        if t + pow(t,2) >total:
            break
        else:
            ans = t
    print(ans)