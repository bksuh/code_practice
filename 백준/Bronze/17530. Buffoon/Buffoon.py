t = int(input())
arr = [int(input()) for _ in range(t)]

carl = arr[0]
if carl == max(arr):
    print('S')
else:
    print('N')