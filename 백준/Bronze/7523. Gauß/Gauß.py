n = int(input())

for _ in range(n):
    a, b = map(int, input().split())
    ans = (b - a +1)*(a+b)//2
    print(f'Scenario #{_+1}:')
    print(ans)
    print()