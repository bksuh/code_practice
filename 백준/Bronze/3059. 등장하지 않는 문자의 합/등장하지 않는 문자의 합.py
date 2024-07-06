n = int(input())
for _ in range(n):
    arr = [i for i in range(ord('A'), ord('Z')+1)]
    a = input()
    for elem in a:
        tmp = ord(elem)-ord('A')
        arr[tmp] = 0
    print(sum(arr))