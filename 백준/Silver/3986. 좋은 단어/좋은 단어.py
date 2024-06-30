n = int(input())

def checker(word):
    arr = []
    for i in range(len(word)):
        if len(arr) == 0:
            arr.append(word[i])
        elif word[i] == arr[-1]:
            arr.pop()
        else:
            arr.append(word[i])
    if len(arr) == 0:
        return True
    return False

cnt=0
for _ in range(n):
    tmp = input()
    if checker(tmp):
        cnt+=1

print(cnt)