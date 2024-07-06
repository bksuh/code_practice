t = int(input())
for _ in range(t):
    val = list(bin(int(input()))[2:])
    val.reverse()
    for i, v in enumerate(val):
        if v == '1':
            print(i, end =' ')
    print()