a = ['a','e','i','o','u']
tar = input()
indi = 0
for c in tar:
    if indi > 0:
        print('', end='')
        indi-=1
        continue
    if c in a:
        indi = 2
        print(c , end='')
        continue
    else:
        print(c , end='')