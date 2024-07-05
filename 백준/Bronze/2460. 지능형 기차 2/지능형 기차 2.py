arr= []
before = 0
for _ in range(10):
    a, b = map(int, input().split())
    before = before - a + b
    arr.append(before)
print(max(arr))