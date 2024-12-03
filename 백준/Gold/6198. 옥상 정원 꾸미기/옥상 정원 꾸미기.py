t = int(input())
building = [int(input()) for _ in range(t)]

stack = []
ans = 0

for b in building:
    while stack and stack[-1] <= b:
        stack.pop()
    stack.append(b)
    
    ans += len(stack) -1 
print(ans)