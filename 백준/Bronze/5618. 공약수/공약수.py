from math import gcd

n= int(input())
arr = list(map(int, input().split()))
if n == 2:
    ans = gcd(arr[0], arr[1])
else:
    ans = gcd(arr[0], gcd(arr[1], arr[2]))

for i in range(1, ans+1):
    if ans % i == 0:
        print(i)