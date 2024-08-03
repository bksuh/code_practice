a, b = map(int, input().split())
answer = ((a + b) * (abs(a - b) + 1)) // 2
print(answer)