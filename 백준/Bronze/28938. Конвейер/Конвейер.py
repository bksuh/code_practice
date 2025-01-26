t = int(input())
arr = list(map(int, input().split()))

ans = sum(arr)

if ans > 0:
    print('Right')
elif ans == 0:
    print('Stay')
else:
    print('Left')