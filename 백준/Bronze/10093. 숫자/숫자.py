arr = []
a, b  = map(int, input().split())
start = min(a,b)
end = max(a, b)
for i in range(start+1, end):
    arr.append(i)
print(len(arr))
print(*arr)