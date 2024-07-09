a, b = map(int, input().split())
arr = [a/b*1000]
n = int(input())
for _ in range(n):
    x, y = map(int, input().split())
    arr.append(x/y*1000)
print(f"{min(arr):.2f}")