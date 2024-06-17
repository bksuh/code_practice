import sys
input = sys.stdin.readline
current = 1
stack, answer, find = [], [], True
n = int(input())
for _ in range(n):
    a = int(input())
    while current<=a:
        stack.append(current)
        answer.append('+')
        current +=1
    if stack[-1] == a:
        stack.pop(-1)
        answer.append('-')


if len(stack):
    print('NO')
else:
    for element in answer:
        print(element)