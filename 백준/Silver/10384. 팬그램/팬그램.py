n = int(input())

for i in range(1,n+1):
    arr = [0 for _ in range(ord('z')-ord('a')+1)]
    tar = input()
    for c in tar:
        if c.isalpha():
            c = c.lower()
            if 0<=ord(c)- ord('a')<=25:
                arr[ord(c)-ord('a')] +=1
            else:
                continue
    ans = set(arr)
    if arr.count(0) == 0 and min(arr)==1:
        print(f'Case {i}: Pangram!')
    elif min(arr) == 2:
        print(f'Case {i}: Double pangram!!')
    elif min(arr) == 3:
        print(f'Case {i}: Triple pangram!!!')
    else:
        print(f'Case {i}: Not a pangram')

