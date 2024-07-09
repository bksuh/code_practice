A = list(map(int, input().split()))
B = list(map(int, input().split()))
winner = 'D'
a, b = 0, 0
for i in range(len(A)):
    if A[i] == B[i]:
        a+=1
        b+=1
    elif A[i] > B[i]:
        a+=3
        winner = 'A'
    else:
        b+=3
        winner = 'B'
print(a, b)
if a>b:
    winner = 'A'
elif a < b:
    winner = 'B'
print(winner)