n = int(input())
x, y = map(int, input().split())
total = x*y
arr = list(map(int, input().split()))
arr.sort(reverse=True)

for i in range(len(arr)):
    total -= arr[i]
    if total <= 0:
        print(i+1)
        break
if total > 0:
    print('STRESS')