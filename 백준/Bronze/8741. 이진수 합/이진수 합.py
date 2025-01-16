k = int(input())
last = int('1'*k, 2)
ans = last*(last+1)//2
print(bin(ans)[2:])