nums = [int(c) for c in input()]
ans = 0

for num in nums:
    ans += pow(num, 5)

print(ans)