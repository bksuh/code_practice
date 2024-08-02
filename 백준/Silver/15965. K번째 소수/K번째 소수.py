import math

def isPrime(x):
    for i in range(2, int(math.sqrt(x)+1)):
        if x % i == 0:
            return False
    return True

n = int(input())
cnt = 0
num = 2
while True:
    if isPrime(num):
        cnt+=1
    if n == cnt:
        print(num)
        break
    num+=1