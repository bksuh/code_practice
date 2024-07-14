n, p = map(int, input().split())
arr = []
current = n
while  True:
    current = (current * n) % p
    if current in arr:
        break
    arr.append(current)
    
print(len(arr)-arr.index(current))