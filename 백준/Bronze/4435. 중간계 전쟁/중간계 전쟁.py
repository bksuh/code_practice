n = int(input())
gan = [1, 2, 3, 3, 4, 10]
sa = [1, 2, 2, 2, 3, 5, 10]
for k in range(n):
    gan_troop  = list(map(int, input().split()))
    sa_troop  = list(map(int, input().split()))
    g, s = 0, 0
    for i in range(len(gan)):
        g += gan[i]*gan_troop[i]
    for j in range(len(sa)):
        s += sa[j]* sa_troop[j]
    print(f'Battle {k+1}: ', end='')
    if g > s:
        print('Good triumphs over Evil')
    elif g==s:
        print('No victor on this battle field')
    else:
        print("Evil eradicates all trace of Good")