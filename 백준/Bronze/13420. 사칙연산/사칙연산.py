t = int(input())

for _ in range(t):
    a, b = input().split('=')
    a = eval(a)
    b = int(b)

    if a == b:
        print('correct')
    else:
        print('wrong answer')        