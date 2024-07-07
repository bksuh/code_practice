n = int(input())
for _ in range(n):
    tmp = int(input())
    print(f'Pairs for {tmp}:', end=' ')
    for i in range(1, tmp//2+1) :
        if i < tmp-i :
            if i != 1 :
                print(',', end=' ')
            print(i, tmp-i, end='')
    print()