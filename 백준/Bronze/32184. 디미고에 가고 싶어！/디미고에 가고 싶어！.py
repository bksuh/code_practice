A, B = map(int, input().split())

if A % 2 == 0 and B % 2 != 0:	
    print((B - A) // 2 + 2)
else:
    print((B - A) // 2 + 1)