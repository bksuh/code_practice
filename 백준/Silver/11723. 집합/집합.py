import sys
s = set()
n = int(sys.stdin.readline())
for _ in range(n):
    instruction = sys.stdin.readline().split()
    if instruction[0] == 'add' and int(instruction[1]) not in s:
        s.add(int(instruction[1]))
    elif instruction[0] == 'remove' and int(instruction[1]) in s:
        s.remove(int(instruction[1]))
    elif instruction[0] == 'check':
        if int(instruction[1]) in s:
            print(1)
        else:
            print(0)
    elif instruction[0] == 'toggle':
        if int(instruction[1]) in s:
            s.remove(int(instruction[1]))
        else:
            s.add(int(instruction[1]))
    elif instruction[0] == 'all':
        s = set([1,2,3,4,5,6,7,8,9,10, 11, 12, 13, 14, 15, 16,17,18,19,20])
    elif instruction[0] =='empty':
        s = set()