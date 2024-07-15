nums = [1,1,2,4,8]
for i in range(65):
    nums.append(nums[i+4]*2 - nums[i])
n = int(input())
for _ in range(n):
    t = int(input())
    print(nums[t])