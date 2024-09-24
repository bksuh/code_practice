a = int(input())
bonus = 0
score = list(input())
result = 0
for i,v in enumerate(score):
    if v == 'O':
        result += (bonus+i+1)
        bonus += 1
    else:
        bonus = 0
print(result)