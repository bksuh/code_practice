n = int(input())
arr = []
ans =[]
for _ in range(n):
    arr.append(input())
if n == 1:
    print(arr[0])
else:
    for i in range(len(arr[0])):
        indi = True
        for j in range(1, n):
            if arr[j-1][i] != arr[j][i]:
                indi = False
        if indi:
            ans.append(arr[0][i])
        else:
            ans.append("?")
    for element in ans:
        print(element, end="")