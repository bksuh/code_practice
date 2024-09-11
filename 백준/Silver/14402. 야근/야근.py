import sys
input = sys.stdin.readline

q = int(input())

check = {} 
overtime =0    
for i in range(q):
  name, data = input().split()
  if data == '-':
    if name not in check or check[name] == 0:
      overtime +=1
    elif name in check:
      check[name] -=1
  elif data == '+':
    if name not in check:    
      check[name] = 1
    else:
      check[name] += 1   

print(sum(check.values()) + overtime)