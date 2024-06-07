a=int(input())
b = int(input())
c = int(input())

arr = [0]*10
result = a*b*c
tmp = [int(c) for c in str(result)]
for i in range(len(tmp)):
    arr[tmp[i]]+=1
for i in range(len(arr)):
    print(arr[i])