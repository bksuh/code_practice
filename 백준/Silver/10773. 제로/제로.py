arr = []
n = int(input())
for _ in range(n):
    tmp = int(input())
    if tmp == 0:
        arr.pop()
    else:
        arr.append(tmp)

print(sum(arr))