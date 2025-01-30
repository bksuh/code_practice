N=int(input())
total=0
for i in range(1,N+1):
    for j in range(i, N//i+1):
        total+=1

print(total)