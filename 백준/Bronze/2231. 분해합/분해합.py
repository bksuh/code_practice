n = int(input())
ans = 0
for num in range(1, n):
    a = [int(c) for c in str(num)]
    result = num + sum(a)
    if result == n:
        ans = num
        break

print(ans)