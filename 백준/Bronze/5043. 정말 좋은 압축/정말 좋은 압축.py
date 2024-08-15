n, b = map(int, input().split())
tmp = pow(2, b+1) - 1
print("yes" if tmp>= n else "no")