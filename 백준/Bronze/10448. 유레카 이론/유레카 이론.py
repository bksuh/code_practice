ans = [i*(i+1)//2 for i in range(1, 45)]
tmp = [0 for i in range(1001)]

for i in ans:
    for j in ans:
        for k in ans:
            if i+j+k <= 1000:
                tmp[i+j+k] = 1

n = int(input())

for _ in range(n):
    t = int(input())
    print(tmp[t])