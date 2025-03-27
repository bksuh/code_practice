t = int(input())
cnt = 0
for i in range(1, t+1):
    if cnt == 6:
        cnt = 0
        print(f'Go!', end=' ')
    print(i, end=' ')
    cnt+=1
        
print('Go!')