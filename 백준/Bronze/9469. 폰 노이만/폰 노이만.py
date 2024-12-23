t = int(input())

for _ in range(t):
    arr = list(map(float, input().split()))
    tmp = arr[2] + arr[3]
    tmp = arr[1] / tmp
    tmp = tmp * arr[4]
    print(int(arr[0]), tmp)