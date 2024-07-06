import sys
input = sys.stdin.readline

n = int(input())
for _ in range(n):
    a, b = map(int, input().rstrip().split())
    target = input().rstrip()
    for c in target:
        tmp = (a*(ord(c)-ord('A'))+b)%26
        print(chr(ord('A')+tmp), end='')
    print()
        