arr = []
for _ in range(10):
    a = int(input())
    tmp = a%42
    arr.append(tmp)
print(len(set(arr)))