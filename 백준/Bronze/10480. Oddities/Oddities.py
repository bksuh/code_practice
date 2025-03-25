t = int(input())

for _ in range(t):
    ans = int(input())
    if ans % 2 == 0:
        print(f"{ans} is even")
    else:
        print(f"{ans} is odd")