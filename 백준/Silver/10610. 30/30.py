n = [int(c) for c in input()]
if 0 in n:
    n.remove(0)
    if sum(n)%3 == 0:
        n.sort(reverse=True)
        print(*n,sep='',end='0')
    else:
        print(-1)
else:
    print(-1)