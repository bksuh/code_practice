arr = []
for _ in range(9):
    tmp = int(input())
    arr.append(tmp)
indi = False
for i in range(len(arr)):
    for j in range(i, len(arr)):
        if i==j:
            continue
        ans = sum(arr)-arr[i]- arr[j]
        if ans == 100:
            arr.pop(i)
            arr.pop(j-1)
            indi = True
            break
    if indi:
        break
arr.sort()
for element in arr:
    print(element)