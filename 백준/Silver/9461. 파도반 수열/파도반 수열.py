n = int(input())
arr = list(int(input()) for _ in range(n))
nums = max(arr)-5
ans = [1,1,1,2,2]
if nums > 0:
    for _ in range(nums):
        ans.append(ans[-1]+ ans[-5])

for elem in arr:
    print(ans[elem-1])
