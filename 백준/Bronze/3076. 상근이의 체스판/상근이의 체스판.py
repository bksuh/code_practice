R, C = map(int, input().split())
A, B= map(int, input().split())

for i in range(R):
    if i%2 == 0:
        for _ in range(A):
            for j in range(C):
                if j%2 == 0:
                    print('X'*B, end='')
                else:
                    print('.'*B, end='')
            print()
    else:
        for _ in range(A):
            for j in range(C):
                if j%2 == 0:
                    print('.'*B, end='')
                else:
                    print('X'*B, end='')
            print()