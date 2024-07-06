arr1 = list(int(input()) for _ in range(10))
arr2 = list(int(input()) for _ in range(10))

arr1.sort()
arr2.sort()

print(arr1[-1]+arr1[-2]+arr1[-3], arr2[-1]+arr2[-2]+arr2[-3])