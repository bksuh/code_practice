ans = 0
n = int(input())
for _ in range(n):
    t = int(input())
    if t % 2 == 1:
        ans +=1
print(ans)