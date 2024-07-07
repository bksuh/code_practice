arr = [0 for _ in range(ord('z')-ord('a')+1)]

while True:
    try:
        a = input()
        for c in a:
            if c == ' ':
                continue
            arr[ord(c)-ord('a')] +=1
    except:
        break
tmp = max(arr)
for i in range(len(arr)):
    if arr[i] == tmp:
        print(chr(ord('a')+ i), end='')