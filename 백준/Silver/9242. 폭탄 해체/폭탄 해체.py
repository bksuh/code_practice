zero = ['***','* *', '* *','* *','***']
one = ['  *','  *', '  *','  *','  *']
two = ['***','  *', '***','*  ','***']
three = ['***','  *', '***','  *','***']
four = ['* *','* *', '***','  *','  *']
five = ['***','*  ', '***','  *','***']
six = ['***','*  ', '***','* *','***']
seven = ['***','  *','  *','  *','  *'] 
eight = ['***','* *', '***','* *','***']
nine = ['***','* *', '***','  *','***']
nums = [zero, one, two, three, four, five, six, seven,eight, nine]
grid = [input() for _ in range(5)]
answer = ''
for j in range(0, len(grid[0])+1, 4):
    tmp = []
    for i in range(5):
        tmp.append(grid[i][j:j+3])
    if tmp in nums:
        answer += str(nums.index(tmp))
    else:
        answer = 'BOOM!!'
        break
if answer == 'BOOM!!':
    print(answer)
elif int(answer) % 6 == 0:
    print('BEER!!')
else:
    print("BOOM!!")
