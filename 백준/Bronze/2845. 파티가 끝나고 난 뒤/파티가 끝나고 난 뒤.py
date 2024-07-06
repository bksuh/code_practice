a, b = map(int, input().split())
ans = a*b

new = list(map(int, input().split()))
for i in range(len(new)):
    new[i] -=ans
print(*new)