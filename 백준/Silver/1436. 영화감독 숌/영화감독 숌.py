import sys
input = sys.stdin.readline

n = int(input())
cnt = 0
start = 665
while True:
    if cnt == n:
        break
    if '666' in str(start):
        cnt+=1
    start +=1
print(start-1)