a = [False, False] + [True]*(318137-1)
prime =[]
for i in range(2, 318138):
    if a[i]:
        prime.append(i)
        for j in range(2*i, len(a), i):
            a[j] = False

super_prime = []

for i in range(len(prime)):
    if prime[i] <= 27449:
        super_prime.append(prime[prime[i]-1])
    else:
        break

n = int(input())

for _ in range(n):
    t = int(input())
    print(super_prime[t-1])