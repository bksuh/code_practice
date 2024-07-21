n = int(input())
tmp = [int(input()) for _ in range(n)]
t = max(tmp)+1
arr = list(i for i in range(t))
for i in range(2, t):
    for j in range(2*i, t, i):
        arr[j] = 0
arr[1] = 0
primes = list(set(arr))[1:]

for t in tmp:
    for prime in primes:
        cnt = 0
        while True:
            if t % prime != 0:
                break

            t //= prime
            cnt +=1
        if cnt !=0:
            print(prime, cnt)
