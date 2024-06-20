import sys
input=sys.stdin.readline
def factorial(n):
    if n>1:
        return n*factorial(n-1)
    else:
        n = 1
        return n
    
n = int(input())
res = list(str(factorial(n)))
res.reverse()
cnt = 0
for i in range(len(res)):
    if res[i] == '0' :
        cnt+=1
    else:
        break
print(cnt)