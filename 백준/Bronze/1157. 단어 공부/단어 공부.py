x = input().lower()
arr = [0]*(ord('z')-ord('a')+1)
for i in range(len(x)):
    arr[ord(x[i])-ord('a')] +=1
tmp = max(arr)
cnt = 0
for i in range(len(arr)):
    if arr[i] == tmp:
        cnt+=1

if cnt>=2:
    print("?")
else:
    print(chr(ord('A')+arr.index(tmp)))