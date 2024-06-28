import sys
indi = False
input = sys.stdin.readline
n = int(input())
arr = [0 for _ in range(0, ord('z')-ord('a')+1)]
for _ in range(n):
    tmp = input().rstrip()
    arr[ord(tmp[0])-ord('a')] +=1
for i in range(len(arr)):
    if arr[i]>=5:
        indi = True
        print(chr(ord('a')+i), end ='')
if not indi:
    print("PREDAJA")
    
    