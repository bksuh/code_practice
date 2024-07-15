digit_word = ['zero', 'one', 'two', 'three', 'four','five','six', 'seven','eight','nine']
a, b = map(int, input().split())
ans = []
for i in range(a, b+1):
    tmp = str(i)
    word = ''
    for digit in tmp:
        word += digit_word[int(digit)] + ' '
    word = word.rstrip()
    ans.append( (i, word))
ans.sort(key= lambda x : x[1])
cnt = 0
for i in range(len(ans)):
    print(ans[i][0], end = ' ')
    cnt +=1
    if cnt==10:
        cnt = 0
        print('\n', end ='')