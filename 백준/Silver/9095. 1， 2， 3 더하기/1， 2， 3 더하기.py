n = int(input())
nums = list(int(input()) for _ in range(n))
arr = [0, 1, 2, 4]
for i in range(4, max(nums)+1):
    arr.append(arr[i-1]+arr[i-2]+arr[i-3])
for elem in nums:
    print(arr[elem])