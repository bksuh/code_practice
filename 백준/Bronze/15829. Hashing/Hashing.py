import sys

n = int(sys.stdin.readline())
arr = list(input())
result = 0
for i in range(n):
    head = int(ord(arr[i])) - 96
    result += head * pow(31, i)

print(result)