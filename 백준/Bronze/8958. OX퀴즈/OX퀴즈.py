a = int(input())
for _ in range(a):
    string = list(input())
    score = 1
    for i in range(len(string)):
        if string[i]=='O':
            string[i] = score
            score +=1
        else:
            score = 1
            string[i] =0
    print(sum(string))