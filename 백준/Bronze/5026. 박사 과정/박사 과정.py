n = int(input())
for _ in range(n):
    a = input()
    if a == 'P=NP':
        print('skipped')
    else:
        x, y = map(int, a.split('+'))
        print(x+y)