a, b = map(int, input().split())
arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))

arr1 += arr2
arr1.sort()
print(*arr1)