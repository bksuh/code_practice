a, b, c = map(int, input().split())
x, y, z = map(int, input().split())

ans1 = 3*a + 20*b + 120*c
ans2 = 3*x + 20*y + 120*z

if ans1 > ans2:
    print("Max")
elif ans1 == ans2:
    print('Draw')
else:
    print("Mel")