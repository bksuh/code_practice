import sys
input = sys.stdin.readline

n = int(input())
arr = list(int(input()) for _ in range(n))
arr.sort(reverse=True)
print(*arr, sep='\n')