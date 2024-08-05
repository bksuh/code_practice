n = int(input())
arr = [i for i in range(1, n+1)]
while True:
    if len(arr) == 1:
        break
    tmp = []
    for j in range(1, len(arr), 2):
        tmp.append(arr[j])
    arr = tmp
print(arr[0])