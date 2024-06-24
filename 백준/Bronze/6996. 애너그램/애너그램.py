import sys
input = sys.stdin.readline

n = int(input())
for _ in range(n):
    a, b = input().rstrip().split()
    a1 = list(a)
    b1 = list(b)
    a1.sort()
    b1.sort()
    if a1 == b1:
        print(f"{a} & {b} are anagrams.")
    else:
        print(f"{a} & {b} are NOT anagrams.")