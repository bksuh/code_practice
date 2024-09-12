n, t = map(int, input().split())
import sys
input = sys.stdin.readline
server = {}
for i in range(t):
    id = input().rstrip()
    server[id] = i
result = [(k, v) for k, v in server.items()]
result.sort(key = lambda x : (x[1]))
if (n > len(result)):
    n = len(result)
for j in range(n):
    print(result[j][0])