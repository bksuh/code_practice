import sys
input = sys.stdin.readline
n = input()
arr = [0, 0, 0, 'ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
ans = 0
for i in range(len(n)):
    for j in range(3, len(arr)):
        if n[i] in arr[j]:
            ans +=j
print(ans)