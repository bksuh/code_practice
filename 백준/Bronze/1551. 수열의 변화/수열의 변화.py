m,n = map(int, input().split())
arr = list(map(int, input().split(',')))

for _ in range(n):
    for i in range(len(arr)-1):
        arr[i] = arr[i+1]- arr[i]
print(*(arr[:m-n]),sep=',')
