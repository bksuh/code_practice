n = int(input())

for _ in range(n):
    cute = 0
    s = input()
    for i in range(len(s)-2):
        if s[i] == 'W' and s[i:i+3] == 'WOW':
            cute += 1
    print(cute)