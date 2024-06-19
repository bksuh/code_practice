arr = list(map(int, input().split()))
area = arr[0]*arr[2]/arr[1]/arr[3]/2
if area == int(area):
    print(1)
else:
    print(0)