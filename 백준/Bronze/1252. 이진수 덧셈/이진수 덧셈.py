a, b = input().split()

a = int(a, 2)
b = int(b,2)
ans = a+b
print(bin(ans)[2::])