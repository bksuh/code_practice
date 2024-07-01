n = int(input())
arr = []
for _ in range(n):
    a, b, c = map(int, input().split())
    if a == b and c == b:
        total = 1000 * a + 10000
        arr.append(total)
    elif a == b or b == c :
        total = 100 * b + 1000
        arr.append(total)
    elif c == a:
        total = 100 * c + 1000
        arr.append(total)
    else:
        total = 100* max(a, b, c)
        arr.append(total)
print(max(arr))