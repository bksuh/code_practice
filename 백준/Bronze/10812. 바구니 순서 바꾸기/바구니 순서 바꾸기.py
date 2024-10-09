n, m =map(int, input().split())

nums = [c for c in range(1, n+1)]

for _ in range(m):
    begin, end, mid = map(int, input().split())
    nums = nums[:begin-1]+nums[mid-1:end]+nums[begin-1:mid-1]+nums[end:]
print(*nums)