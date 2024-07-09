i = 1
while True:
    n = int(input())
    if n==0:
        break
    n *=3
    if n%2 == 0:
        n //=2
        print(f"{i}. even ", end='')
    else:
        n = (n+1)//2
        print(f"{i}. odd ", end='')
    n *=3
    n //=9
    print(n)
    i+=1