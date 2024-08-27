n = int(input())
for i in range(n):
    tmp = list(input().split())
    ans = ' '.join(tmp[::-1])
    print(f"Case #{i+1}: {ans}")