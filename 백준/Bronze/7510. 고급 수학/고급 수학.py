n = int(input())

for i in range(n):
    arr = list(map(int, input().split()))
    arr.sort()
    print(f"Scenario #{i+1}:")
    print("yes" if pow(arr[2],2) == pow(arr[0],2) + pow(arr[1],2) else "no")
    print()