n = int(input())
tar = input()
arr = [0 for _ in range(ord('Z')-ord('A')+1)]
for i in range(n):
    arr[i] = int(input())
stack = []

for c in tar:
    if c =='+':
        ans = stack[-2] + stack[-1]
        stack.pop()
        stack.pop()
        stack.append(ans)

    elif c == '-':
        ans = stack[-2] - stack[-1]
        stack.pop()
        stack.pop()
        stack.append(ans)

    elif c == '*':
        ans = stack[-2] * stack[-1]
        stack.pop()
        stack.pop()
        stack.append(ans)

    elif c == '/':
        ans = stack[-2] / stack[-1]
        stack.pop()
        stack.pop()
        stack.append(ans)
    else:
        stack.append(arr[ord(c)-ord('A')])

print(f"{stack[0]:.2f}")