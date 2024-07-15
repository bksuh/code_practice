n = int(input())
nums = {}

for _ in range(n):
    t = int(input())
    if t in nums:
        nums[t] +=1
    else:
        nums[t] = 1
ans = []
for k, v in nums.items():
    ans.append((k, v))
ans.sort(key= lambda x : (-x[1], x[0]))
print(ans[0][0])