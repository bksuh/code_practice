n = int(input())
for _ in range(n):
    ans = int(input())
    action = input()
    for c in action:
        if c =='c':
            ans += 1
        else:
            ans -= 1
    print(f"Data Set {_+1}:")
    print(ans)
    print()