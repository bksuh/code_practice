import sys

N = int(sys.stdin.readline().strip())
mailboxes = sys.stdin.readline().strip()

for K in range(1, N + 1):
    seen = set() 
    unique = True
    for i in range(N - K + 1):
        substring = mailboxes[i:i + K]
        if substring in seen:
            unique = False
            break
        seen.add(substring)

    if unique:
        print(K)
        break