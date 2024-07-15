from math import gcd

n = int(input())
arr = list(map(int, input().split()))
for i in range(1, n):
    print(f"{arr[0]//gcd(arr[0], arr[i])}/{arr[i]//gcd(arr[0], arr[i])}")