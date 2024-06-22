import sys
input = sys.stdin.readline
n = int(input())

for i in range(n):
    print(' '* i , end='')
    print('*'*(-2*i +2*n-1)) 