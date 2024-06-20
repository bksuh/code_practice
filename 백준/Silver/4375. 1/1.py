import sys
input = sys.stdin.readline

def check(n):
    cnt = 1
    while True:
        tmp = int('1'*cnt)
        if tmp%n == 0:
            break
        cnt+=1
    return cnt
while True:
    try:
        n = int(input())
    except:
        break
    print(check(n))