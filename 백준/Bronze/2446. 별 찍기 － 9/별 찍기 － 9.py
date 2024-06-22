import sys
input = sys.stdin.readline
n = int(input())

for i in range(n):
    
    print(' '* i, end ='')
    print('*' * (2*(n-i)-1))
for i in range(n-2, -1,-1):
    print(' '*i, end ='')
    print('*' * (2*(n-i)-1))
