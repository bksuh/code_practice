n = int(input())

arr = [input() for _ in range(n)]
t = int(input())

if t == 1:
    print(*arr, sep='\n')

elif t == 2:
    print(*[i[::-1] for i in arr], sep='\n')

else:
    print(*arr[::-1], sep='\n')
